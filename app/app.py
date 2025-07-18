import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import json
from recommender.recommender import load_topic_graph, recommend_next_topics


# Load topic graph
topic_graph = load_topic_graph("data/topic_graph.json")

all_topics = []
for topics in topic_graph.values():
    all_topics.extend(topics)

st.title("Personalized Study Plan Recommender")

# User Input: Select topics studied
st.header("Select the topics you have studied:")
selected_topics = st.multiselect("Topics Studied:", all_topics)

# User Input: Enter confidence levels
confidence_levels = []
for topic in selected_topics:
    confidence = st.slider(f"Confidence in {topic} (1=Low, 5=High)", 1, 5, 3)
    confidence_levels.append(confidence)

# User Input: Learning style
learning_style = st.selectbox("Select Your Learning Style:", ["Visual", "Auditory", "Text"])

# Button to generate recommendations
if st.button("Generate Recommendations"):
    recommendations = recommend_next_topics(selected_topics, confidence_levels, topic_graph)
    st.subheader("Recommended Next Topics:")
    for rec in recommendations:
        st.write("- ", rec)
