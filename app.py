import streamlit as st
import { CohereEmbeddings } from "@langchain/cohere";

const embeddings = new CohereEmbeddings({
  apiKey: "GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg", // In Node.js defaults to process.env.COHERE_API_KEY
  batchSize: 48, // Default value if omitted is 48. Max value is 96
  model: "embed-english-v3.0",
});

# 初期設定
st.set_page_config(page_title="プロンプト生成", layout="centered")
st.write(embeddings)
