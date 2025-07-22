import streamlit as st
from search import search

# 🏛️ Roman waterfall background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpaperflare.com/static/476/567/884/ai-art-temple-ancient-temple-waterfall-rome-wallpaper.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .chatbox {
        background-color: rgba(255,255,255,0.85);
        padding: 10px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏛️ Tibeirus Shipping Assistant")

st.text_area("📜 Enter log entries here (optional):")

query = st.chat_input("🔍 Ask a question about the Roman voyages:")

if query:
    result = search(query)
    st.markdown(f"<div class='chatbox'>💬 {result}</div>", unsafe_allow_html=True)
