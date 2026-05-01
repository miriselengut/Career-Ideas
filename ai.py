import streamlit as st
from openai import AzureOpenAI

def ai_convo():
    openai_api_key = st.secrets["AZURE_OPENAI_API_KEY"]
    openai_api_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:
        client = AzureOpenAI(
            api_key=openai_api_key,
            api_version="2024-12-01-preview",
            azure_endpoint=openai_api_endpoint
        )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Have a question?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        stream = client.chat.completions.create(
            model=st.secrets["AZURE_OPENAI_MODEL"],
            messages=[
                {"role": "system", "content": ''' You are to help direct people to their proper career. 
                                            You can discuss things like salary, (both realistic and idealistic), 
                                            skill set and prior education. You may also mention things like work envoirment 
                                            and job description. If a user asks about something else, politely bring the 
                                            conversation back to careers.'''},
                *[{"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages]
            ],
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})