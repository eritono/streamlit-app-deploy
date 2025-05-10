import streamlit as st
import langchain
import os

# 💡 LangChainのバージョンを表示（ここで確認！）
st.write("LangChain version:", langchain.__version__)

# タイトル
st.title("Hello Streamlit!")
import streamlit as st

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

# 🔐 APIキーをsecrets.tomlから読み込み
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 🖥 タイトル・説明
st.title("育児サポート AI アシスタント")
st.markdown("""
このアプリでは、あなたの育児に関するお悩みにAIが専門家として回答します。  
以下の専門家タイプを選び、相談内容を入力してください。
""")

# 🎛 専門家選択ラジオボタン
expert_type = st.radio("相談したい専門家を選んでください：", ["栄養士", "ストレス管理士"])

# ✍️ 入力欄
user_input = st.text_area("ご相談内容を入力してください：", height=150)

# 💬 LLMからの回答を取得する関数
def get_response(user_input, expert_type):
    if expert_type == "栄養士":
        system_msg = "あなたは子どもの栄養に詳しい栄養士です。親からの相談にやさしく丁寧に答えてください。"
    elif expert_type == "ストレス管理士":
        system_msg = "あなたは育児ストレスに詳しい専門家です。心のケアに関するアドバイスをしてください。"
    else:
        system_msg = "あなたは親の育児に関する専門家です。一般的なアドバイスを提供してください。"

    chat = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_input)
    ]
    response = chat(messages)
    return response.content

# 🚀 実行ボタン
if st.button("AIに相談する"):
    if user_input.strip():
        with st.spinner("AIが回答中..."):
            answer = get_response(user_input, expert_type)
            st.success("回答：")
            st.write(answer)
    else:
        st.warning("ご相談内容を入力してください。")
        


