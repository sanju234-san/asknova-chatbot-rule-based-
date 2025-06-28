import streamlit as st

responses = {
    "hii": "hi there sanjeevni, how can I help you?",
    "how are you": "I am a chatbot; I can't feel anything.",
    "what is your name": "My name is Asknova.",
    "bye": "Bye! Have a nice day.",
    "help": "I am here to help you.",
    "in which college do i study": "You study in SRM University.",
    "what is my name": "Your name is Sanjeevni.",
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")


st.title("Asknova: Your Personal Chatbot")


if "history" not in st.session_state:
    st.session_state.history = []


user_input = st.text_input("You: ", key="input")


if user_input:
    response = get_response(user_input)
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"Asknova: {response}")


for chat in st.session_state.history:
    st.write(chat)
