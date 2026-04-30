# import streamlit as st
# from streamlit_extras import floating_button
# from openai import AzureOpenAI
# from streamlit_extras.floating_button import *


# # AI converstaion
# st.header("💬 Talk to a Pesach Bot!")
# openai_api_key = st.secrets["AZURE_OPENAI_API_KEY"]
# openai_api_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]

# def ai_convo():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.", icon="🗝️")
#     else:
#         client = AzureOpenAI(
#             api_key=openai_api_key,
#             api_version="2024-12-01-preview",
#             azure_endpoint=openai_api_endpoint
#         )

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     if prompt := st.chat_input("Have a question?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         stream = client.chat.completions.create(
#             model=st.secrets["AZURE_OPENAI_MODEL"],
#             messages=[
#                 {"role": "system", "content": "Youa are a helpful career finder. You are using peoples skill sets (specificlly their top 3 skills), previous education, and ideal salary to help them pick the correct job for them."},
#                 *[{"role": m["role"], "content": m["content"]}
#                     for m in st.session_state.messages]
#             ],
#             stream=True,
#         )

#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})

