import streamlit as st


# Configure page
st.set_page_config(page_title="Dental Assistant", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .stMarkdown {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Your Dental Health Assistant")
st.markdown("Ask me anything about dental health and hygiene")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"<div class='{message['role']}-message'>{message['content']}</div>", 
                   unsafe_allow_html=True)

if prompt := st.chat_input("Ask about dental health..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = query_with_langchain(prompt)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})