import streamlit as st
from langchain_cohere import CohereEmbeddings

# CohereEmbeddingsの初期化
embeddings = CohereEmbeddings(
    api_key="GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg",  # Node.jsではprocess.env.COHERE_API_KEYがデフォルト
    batch_size=48,  # 省略時のデフォルト値は48。最大値は96
    model="embed-english-v3.0"
)

# 初期設定
st.set_page_config(page_title="プロンプト生成", layout="centered")
st.write(embeddings)
