import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from typing import List


def bag_of_words(texts: List[str]) -> pd.DataFrame:
    """
    Converts a list of text strings into a Bag of Words representation.

    Implementation Tips:
    1. Initialize CountVectorizer with appropriate parameters
    2. Use fit_transform to create the BoW matrix
    3. Convert the sparse matrix to a dense format if needed
    4. Create a DataFrame with words as columns and documents as rows
    5. Consider handling empty texts or texts with only stop words
    6. You might want to explore CountVectorizer parameters like max_features or min_df

    Args:
    texts (list): A list of text strings.

    Returns:
    DataFrame: A DataFrame representing the Bag of Words model.
    """
    
    return df


if __name__ == "__main__":
    texts = ["Converts a list of text strings into a Bag of Words representation", \
             "The words tha changed the strings",\
             "Your duty words of the heart",
             "The Bag full of strings"]
    print(bag_of_words(texts))
    
