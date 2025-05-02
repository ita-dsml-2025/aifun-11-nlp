# Natural Language Processing

## Setup

Before performing the tasks, you need to set up the development environment.

### Creating a Python virtual environment

1. For Windows:
    ```powershell
    python -m venv venv
    ```

2. For Linux/macOS:
    ```bash
    python3 -m venv venv
    ```

### Activating the virtual environment

1. For Windows:
    ```powershell
    .\venv\Scripts\activate
    ```

2. For Linux/macOS:
    ```bash
    source venv/bin/activate
    ```

> [!NOTE]
> After activating the virtual environment, you will see the `(venv)` prefix in front of the command line.

### Installing the required packages from the `requirements.txt` file

1. For both systems:
    ```bash
    pip install -r requirements.txt
    ```

---

## Tasks

### Prerequisites
1. Set up a Python virtual environment as described in the Setup section above
2. Install required packages from `requirements.txt`

### Task 1: Text Cleaning and Tokenization

Text preprocessing is a crucial first step in any NLP pipeline. In this task, you will implement a function `clean_and_tokenize(text)` that prepares raw text for further analysis. The function should remove unnecessary characters (like punctuation), standardize the text (e.g., by converting to lowercase), and split it into individual words (tokens). This process helps ensure consistency and improves the performance of downstream NLP tasks.

#### Implementation Requirements
- Remove all punctuation from the text
- Convert text to lowercase
- Split text into individual words (tokens)
- Return a list of cleaned tokens

### Task 2: Stemming and Lemmatization

Reducing words to their base or root form is essential for many NLP applications. In this task, you will create a function `stem_and_lemmatize(tokens)` that processes a list of tokens in two ways: stemming (cutting words down to their root form) and lemmatization (reducing words to their dictionary form). You will use NLTK's tools for both. The function should return a dictionary showing the original, stemmed, and lemmatized versions of the tokens, which can help you understand the differences between these two techniques.

#### Implementation Requirements
- Use NLTK's `PorterStemmer` for stemming
- Use NLTK's `WordNetLemmatizer` for lemmatization
- Return a dictionary with three keys:
  - "original": list of original tokens
  - "stemmed": list of stemmed tokens
  - "lemmatized": list of lemmatized tokens

### Task 3: Implementing Bag of Words (BoW)

The Bag of Words model is a foundational technique for representing text data numerically. In this task, you will implement a function `bag_of_words(texts)` that takes a list of text documents and converts them into a matrix of word counts. This representation is useful for many machine learning algorithms. You'll use scikit-learn's `CountVectorizer` to automate the process and output the result as a pandas DataFrame for easy inspection and further analysis.

#### Implementation Requirements
- Use scikit-learn's CountVectorizer
- Convert the output to a pandas DataFrame
- Words should be columns, documents should be rows
- Values should represent word frequencies

### Task 4: Calculating TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical measure used to evaluate how important a word is to a document in a collection. In this task, you will implement a function `calculate_tfidf(texts)` that transforms a list of text documents into their TF-IDF representations. This helps highlight words that are unique and meaningful in each document. You'll use scikit-learn's `TfidfVectorizer` and present the results as a pandas DataFrame.

#### Implementation Requirements
- Use scikit-learn's TfidfVectorizer
- Convert the output to a pandas DataFrame
- Words should be columns, documents should be rows
- Values should represent TF-IDF scores

### Task 5: Training a Word2Vec Model for Text Representation

Word2Vec is a powerful technique for learning vector representations of words, capturing semantic relationships between them. In this task, you will implement two functions: `train_word2vec(sentences)` to train a Word2Vec model on a list of tokenized sentences, and `find_similar_words(model, word)` to retrieve the most similar words to a given word using the trained model. This will help you explore how words relate to each other in vector space and understand the basics of word embeddings.

#### Implementation Requirements
- Use gensim's Word2Vec implementation
- Train the model on provided sentences
- Implement find_similar_words to return top 5 most similar words
- Return both the trained model and similarity results
