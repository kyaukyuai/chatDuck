<h1 align="center">🐤 chatDuck - chatting with your DuckDB</h1>

This application is a straightforward tool that enables users to interact with their DuckDB through natural language queries.
It serves as a gateway to the 'Modern Data Stack in a Box with LLM' concept,
it is intended to be used in conjunction with [Modern Data Stack in a box with dbt-duckdb and Apache Superset](https://github.com/kyaukyuai/jaffle_shop_duckdb_superset).

Developed using [Streamlit](https://streamlit.io/), [DuckDB](https://duckdb.org/), [ChromaDB](https://www.trychroma.com/), [LangChain](https://www.langchain.com/), and [OpenAI](https://openai.com/).

https://github.com/kyaukyuai/chatDuck/assets/1140707/ac2c77fe-c9b9-4b11-a3da-10b53521c060

## Table of Contents

- [🚀 'Modern Data Stack in a Box with LLM' concept](#concept)
- [🌟 Features](#features)
- [🛠️ Getting Started](#getting-started)
- [🤝 Special Thanks](#special-thanks)

## Concept

It serves as a gateway to the 'Modern Data Stack in a Box with LLM' concept,
it is intended to be used in conjunction with [Modern Data Stack in a box with dbt-duckdb and Apache Superset](https://github.com/kyaukyuai/jaffle_shop_duckdb_superset).

![MDS-in-a-Box-with-LLM](https://github.com/kyaukyuai/chatDuck/assets/1140707/d07caf0d-dd46-48f6-a47e-49317ab6784f)


## Features

- **Conversational AI**: Harnesses ChatGPT to translate natural language into precise SQL queries.
- **Conversational Memory**: Retains context for interactive, dynamic responses.
- **DuckDB Integration**: Offers seamless, real-time data insights straight from your DuckDB.
- **Self-healing SQL**: Proactively suggests solutions for SQL errors, streamlining data access.

## Getting Started

1. Set up your `OPENAI_API_KEY` and `DUCKDB_DATABASE` in `.streamlit/secrets.toml`.
2. To run the application, use the following command:
   ```bash
   make run
   ```
3. Access the application in your web browser at http://localhost:8501.

## Special Thanks

- [Modern Data Stack in a Box with DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
- [kaarthik108/snowChat](https://github.com/kaarthik108/snowChat)
