import streamlit as st
from transformers import pipeline

sentiment_pipe = pipeline('sentiment-analysis')

def main():
    st.title("Sentiment Analyzer")

    user_input = st.text_input("Enter your text")

    if st.button("Get Sentiment"):
        if user_input:
            result = sentiment_pipe(user_input)

            st.write(result[0]['label'])

if __name__ == "__main__": 
    main()