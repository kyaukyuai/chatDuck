from typing import Callable, Optional
from pydantic import BaseModel
import streamlit as st

from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

from src.template import CONDENSE_QUESTION_PROMPT, QA_PROMPT

CHROMA_DB_DIRECTORY = "./db/chroma_db"
COLLECTION_NAME = "schema_collection"
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


class ModelConfig(BaseModel):
    callback_handler: Optional[Callable] = None


class ModelManager:
    def __init__(self, config: ModelConfig):
        self.config = config
        self.q_llm = None
        self.llm = None
        self.setup()

    def setup(self):
        self.q_llm = OpenAI(
            temperature=0.1,
            openai_api_key=OPENAI_API_KEY,
            model_name="gpt-3.5-turbo-16k",
            max_tokens=500,
        )

        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo-16k",
            temperature=0.5,
            openai_api_key=OPENAI_API_KEY,
            max_tokens=500,
            callbacks=[self.config.callback_handler]
            if self.config.callback_handler
            else [],
            streaming=True,
        )

    def get_chain(self, vectorstore: Chroma):
        if not self.q_llm or not self.llm:
            raise ValueError("Models have not been properly initialized.")
        question_generator = LLMChain(llm=self.q_llm, prompt=CONDENSE_QUESTION_PROMPT)
        doc_chain = load_qa_chain(llm=self.llm, chain_type="stuff", prompt=QA_PROMPT)
        return ConversationalRetrievalChain(
            retriever=vectorstore.as_retriever(),
            combine_docs_chain=doc_chain,
            question_generator=question_generator,
        )


def load_chain(callback_handler=None):
    embeddings = OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY,
        model="text-embedding-ada-002",
    )
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIRECTORY,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
    )

    config = ModelConfig(
        openai_api_key=OPENAI_API_KEY,
        callback_handler=callback_handler,
    )
    model = ModelManager(config)
    return model.get_chain(vectorstore)
