import json
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Load the JSON-structured articles
with open('articles.json', 'r') as file:
    articles = json.load(file)

# Extract the bodies and slugs from the articles
bodies = [article['body'] for article in articles]
slugs = [article['slug'] for article in articles]

# Encode the article bodies
body_embeddings = model.encode(bodies)

def get_related_articles(target_slug, num_articles):
    target_index = slugs.index(target_slug)
    target_embedding = body_embeddings[target_index].reshape(1, -1)
    # Compute cosine similarity between the target body embedding and all other body embeddings
    similarity_scores = cosine_similarity(target_embedding, body_embeddings)[0]
    # Sort the similarity scores in descending order
    sorted_indices = similarity_scores.argsort()[::-1]
    # Retrieve the top 'num_articles' related slugs
    related_slugs = [slugs[idx] for idx in sorted_indices[1:num_articles+1]]
    return related_slugs

# Example usage
target_slug = 'introduction-to-machine-learning'
num_articles = 5

related_slugs = get_related_articles(target_slug, num_articles)
print(related_slugs)