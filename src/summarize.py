"""Summarize a body of text."""
import copy
from typing import List
from collections import defaultdict as ddict

from textblob import TextBlob, Sentence
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

def summarize(tldr: str) -> List[str]:
    """Summarize a body of text."""
    text = TextBlob(tldr)
    sentences = text.sentences

    preprocessed_sentences = preprocess_sentences(sentences)

    # TODO
    word_scores = score_words_for_significance(preprocessed_sentences)

    # TODO: Should return a dict[index] -> score
    sentence_scores = score_sentences(preprocessed_sentences, word_scores)

    # TODO: average scores

    # TODO: Return sentences filtered if sentence_scores[index] >= avg + threshold

    return sentences

def preprocess_sentences(sentences: List[Sentence]) -> List[List[str]]:
    """Clean up text for summarization."""
    sents = []
    for sent in sentences:
        significant_words = [word for word in sent.tokens if word not in stopwords]
        sents.append(significant_words)

    # TODO: Lemmetize, find references...
    
    return sents
    
if __name__ == '__main__':
    print(summarize('hello my dude. what is the meaning of this?'))