import streamlit as st

st.title("Psychological Sentiment Analyzer")

st.write("Upload text or enter your thoughts, and the model will analyze sentiment.")

# Example input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip():
        st.success(f"Your input: {user_input}")
        # TODO: Call your sentiment model function here
        st.info("Sentiment result will be displayed here")
    else:
        st.warning("Please enter some text.")
