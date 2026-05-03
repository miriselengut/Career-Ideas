import streamlit as st
from openai import AzureOpenAI

def ai_convo(education_level, salary, skill_one, skill_two, skill_three, query_response):
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
        with st.chat_message(message["role"], avatar = "🕵️"):
            st.markdown(message["content"])

    prompt = st.chat_input(f"Ask me about a job that can make ${salary}, with {education_level.lower()}")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        stream = client.chat.completions.create(
            model=st.secrets["AZURE_OPENAI_MODEL"],
            messages=[
                {"role": "system", "content": f''' You help guide people toward suitable career paths. 
                                            You can discuss things like salary, whether or not it is realistic, 
                                            skill set and previous education. The user's previous education consists of
                                            {education_level}, wants a salary of {salary}, skill set includes
                                            {skill_one}, {skill_two} and {skill_three}. The current jobs that came up for the
                                            user are {query_response}. You may discuss mention things like work environment 
                                            and job description. If a user asks about something else, politely bring the 
                                            conversation back to careers. Do not disscuss anything that isn't career related'''},
                *[{"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages]
            ],
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
