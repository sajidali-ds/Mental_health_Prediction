import streamlit as st
import joblib
import re

from nltk.stem import PorterStemmer

model = joblib.load("models/tfidf_svm.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

stemmer = PorterStemmer()
def preprocess_text(text):
    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    text = " ".join(
        stemmer.stem(word)
        for word in text.split()
    )

    return text

st.title("🧠 Mental Health Classification")

st.write(
    "Enter a statement and the model will predict "
    "the mental health category."
)

text = st.text_area(
    "Enter your statement:",
    placeholder="Example: I am feeling nervous and restless..."
)

if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter a statement.")

    else:
        clean_text = preprocess_text(text)

        vector = tfidf.transform([clean_text])

        prediction = model.predict(vector)[0]

        # st.success(
        #     f"Predicted Category: **{prediction}**"
        # )
        if(prediction=='Normal'):
            st.success(f"Predicted Category: **{prediction}**")
        else:
            st.error( f"Predicted Category: **{prediction}**")