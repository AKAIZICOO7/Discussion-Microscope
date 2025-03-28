import streamlit as st
import pandas as pd
import plotly.express as px
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title and description
st.title("Discussion Microscope")
st.write("Analyze and visualize online discussions with topic classification using spaCy.")

# Load spaCy model
@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

# Predefined topics and keywords
TOPIC_KEYWORDS = {
    "Technology": ["AI", "machine learning", "software", "hardware", "programming"],
    "Health": ["medicine", "doctor", "healthcare", "fitness", "disease"],
    "Finance": ["stocks", "investment", "money", "banking", "economy"],
    "Education": ["school", "university", "learning", "teaching", "students"],
    "Sports": ["football", "basketball", "cricket", "tennis", "athlete"]
}

# File upload
uploaded_file = st.file_uploader("Upload a discussion dataset (CSV format)", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(data.head())

    # Topic Classification
    st.subheader("Topic Classification")
    def classify_topic(text):
        doc = nlp(text)
        topic_scores = {topic: sum(1 for token in doc if token.text.lower() in keywords)
                        for topic, keywords in TOPIC_KEYWORDS.items()}
        return max(topic_scores, key=topic_scores.get) if topic_scores else "Unknown"

    data['Topic'] = data['text'].apply(classify_topic)
    st.write("Topic Classification Results:")
    st.dataframe(data[['text', 'Topic']])

    # Visualization: Topic Distribution
    st.subheader("Topic Distribution")
    topic_counts = data['Topic'].value_counts().reset_index()
    topic_counts.columns = ['Topic', 'Count']
    fig = px.bar(topic_counts, x='Topic', y='Count', color='Topic', title="Topic Distribution")
    st.plotly_chart(fig)

    # Visualization: Word Cloud for Topics
    st.subheader("Word Cloud for Topics")
    for topic in TOPIC_KEYWORDS.keys():
        st.write(f"Word Cloud for {topic}")
        topic_text = " ".join(data[data['Topic'] == topic]['text'])
        if topic_text:
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(topic_text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot(plt)
