import re
from nltk.tokenize import word_tokenize
from typing import List


def clean_and_tokenize(text: str) -> List[str]:
    """
    Cleans the input text by removing punctuation and converting it to lowercase,
    then tokenizes it into individual words.

    Implementation Tips:
    1. You can use either:
       - Regular expressions (re module) to remove punctuation:
         * Use re.sub() to replace punctuation with empty string
         * Example pattern: r'[^\w\s]' matches any character that is not a word character or whitespace
         * You can also use string.punctuation from the string module for a list of punctuation characters
       - NLTK's word_tokenize which handles punctuation as separate tokens
    2. Convert the text to lowercase using string methods
    3. Use NLTK's word_tokenize to split the text into words
    4. Consider handling edge cases like empty strings or strings with only punctuation
    5. If using NLTK's approach, you'll need to filter out punctuation tokens after tokenization

    Args:
    text (str): The input text string.

    Returns:
    list: A list of tokens (words).
    """
   
    return tokens


if __name__ == "__main__":
    print(clean_and_tokenize("Cleans the input text by removing punctuation and converting it to lowercase, \
    then tokenizes it into individual words."))

