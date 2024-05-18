import asyncio
import platform

# To prevent Playwright from crashing on windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

GRAPH_CONFIG = {
    "llm": {
        "model": "ollama/llama3",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434"
    },
    "verbose": True,
}

st.title("Web Scraping AI Agent")
st.caption("This app allows you to scrape a website using the llama3 model")

url = st.text_input("Enter the URL of the website you want to scrape")
user_prompt = st.text_input("What would you like the AI agent to scrape from the website?")


smart_scrape_graph = SmartScraperGraph(
    prompt=user_prompt,
    source=url,
    config=GRAPH_CONFIG
)

if st.button("Scrape"):
    result = smart_scrape_graph.run()
    st.write(result)