from gensim.models import Word2Vec
import nltk
from typing import List, Tuple, Any

# Download required NLTK resources
nltk.download('punkt')


# Define example sentences
sentences = [
    ['i', 'love', 'nlp'],
    ['nlp', 'is', 'fun'],
    ['deep', 'learning', 'is', 'a', 'subset', 'of', 'machine', 'learning'],
    ['machine', 'learning', 'is', 'fun'],
    ['nlp', 'can', 'be', 'challenging'],
    ['artificial', 'intelligence', 'is', 'related', 'to', 'nlp']
]


# Function to train Word2Vec model
def train_word2vec(sentences: List[List[str]]) -> Word2Vec:
    """
    Trains a Word2Vec model on a list of tokenized sentences.

    Implementation Tips:
    1. Initialize Word2Vec with appropriate parameters:
       - vector_size: dimension of the word vectors (typically 100-300)
       - window: maximum distance between current and predicted word
       - min_count: ignore words with frequency lower than this
       - workers: number of CPU cores to use
       - sg: 0 for CBOW, 1 for skip-gram (skip-gram is better for small datasets)
    2. Use the sentences directly as they are already tokenized
    3. Consider adjusting parameters based on your dataset size:
       - Larger datasets can use larger vector_size and window
       - Smaller datasets might need smaller vector_size and window
    4. The model will learn word embeddings that capture semantic relationships:
       - Words used in similar contexts will have similar vectors
       - You can perform vector arithmetic (e.g., king - man + woman ≈ queen)
    5. Note that more training data generally leads to better word embeddings
    6. After training, you can save the model using model.save() for later use

    Args:
    sentences (list of list of str): A list of tokenized sentences.

    Returns:
    Word2Vec: A trained Word2Vec model.
    """
    # Initialize and train the Word2Vec model
   
    return model


# Function to find similar words
def find_similar_words(model: Word2Vec, word: str) -> List[Tuple[str, float]]:
    """
    Finds the most similar words to a given word using a trained Word2Vec model.

    Implementation Tips:
    1. Use the model's most_similar method to find similar words:
       - model.wv.most_similar(word) returns similar words and their cosine similarity scores
       - The scores range from -1 to 1, with 1 being most similar
    2. Handle cases where the word might not be in the vocabulary:
       - Check if word in model.wv.key_to_index
       - Return an empty list or raise an exception if word not found
    3. Consider limiting the number of similar words returned:
       - Use topn parameter in most_similar to control number of results
    4. The similarity scores indicate how closely related the words are:
       - Higher scores mean more similar words
       - Scores close to 1 indicate very similar words
       - Scores close to 0 indicate unrelated words
    5. Words with higher similarity scores are more semantically related:
       - They often appear in similar contexts
       - They might be synonyms or related concepts
    6. You can also find words that don't match using model.wv.doesnt_match()

    Args:
    model (Word2Vec): A trained Word2Vec model.
    word (str): The word to find similar words for.

    Returns:
    list: A list of tuples with similar words and their similarity scores.
    """
    return model


# Train Word2Vec model on the sentences
model = train_word2vec(sentences)


similar_words = find_similar_words(model, 'nlp')
print("Words similar to 'nlp':")
for word, score in similar_words:
    print(f"{word}: {score:.4f}")

similar_words = find_similar_words(model, 'learning')
print("\nWords similar to 'learning':")
for word, score in similar_words:
    print(f"{word}: {score:.4f}")
