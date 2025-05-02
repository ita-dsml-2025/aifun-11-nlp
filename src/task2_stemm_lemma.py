from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
from typing import List, Dict, Any

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')


def stem_and_lemmatize(tokens: List[str]) -> Dict[str, List[str]]:
    """
    Applies stemming and lemmatization to the input tokens.

    Implementation Tips:
    1. Initialize PorterStemmer and WordNetLemmatizer objects
    2. For stemming, apply the stemmer to each token
    3. For lemmatization, use the lemmatizer on each token
    4. Note that lemmatization might require additional parameters for better results
    5. Consider handling empty token lists

    Args:
    tokens (list): A list of tokens (words).

    Returns:
    dict: A dictionary with original, stemmed, and lemmatized tokens.
    """
    
    return {
        "original": tokens,
        "stemmed": stemmed,
        "lemmatized": lemmatized
    }


if __name__ == "__main__":
    print(stem_and_lemmatize(['goes', 'worlds', 'done', 'being', 'undefined']))
