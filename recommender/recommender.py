import json

def load_topic_graph(path):
    with open(path, 'r') as file:
        return json.load(file)

def recommend_next_topics(topics_studied, confidence_levels, topic_graph):
    recommendations = []

    for category, topics in topic_graph.items():
        for idx, topic in enumerate(topics):
            if topic not in topics_studied:
                recommendations.append(topic)
            else:
                # Recommend revision if confidence is low (below 3)
                if idx < len(confidence_levels) and int(confidence_levels[idx]) < 3:
                    recommendations.append(f"Revise: {topic}")
                    
    return recommendations
if __name__ == "__main__":
    topic_graph = load_topic_graph("data/topic_graph.json")

    # Example student data
    topics_studied = ["Linear Regression", "CNN Basics"]
    confidence = [4, 2]

    result = recommend_next_topics(topics_studied, confidence, topic_graph)

    print("Recommended Topics:", result)
