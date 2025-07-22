from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Shipping log data
text = """
Apollo carried 300 jars of wine on July 10.
Hermes arrived in Alexandria on August 3.
Zephyr departed from Corinth with olive oil on July 15.
The crew of Apollo reported calm seas and favorable winds.
Hermes transported textiles and spices from Carthage.
Zephyr encountered rough seas near Crete.
Apollo docked in Rome on July 12.
Hermes left Alexandria on August 5.
Zephyr returned to Corinth on July 20.
Apollo was inspected by the port authority on July 11.
"""

# Convert into clean sentences
chunks = [line.strip() for line in text.split('\n') if line.strip()]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Turn sentences into embeddings
embeddings = model.encode(chunks)

# Create FAISS index for similarity search
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Define the search function
def search(query, top_k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    results = [chunks[i] for i in indices[0]]
    return results[0]  # returns top match
br