"""Summarize a body of text."""
from typing import List
from collections import defaultdict as ddict

from textblob import TextBlob
from nltk.corpus import stopwords

def summarize(tldr: str) -> List[str]:
    """Summarize a body of text."""
    text = TextBlob(tldr)
    sentences = text.sentences

    # TODO
    preprocessed_sentences = preprocess_sentences(sentences)

    # TODO
    word_scores = score_words_for_significance(preprocessed_sentences)

    # TODO: Should return a dict[index] -> score
    sentence_scores = score_sentences(preprocessed_sentences, word_scores)

    # TODO: average scores

    # TODO: Return sentences filtered if sentence_scores[index] >= avg + threshold

    return sentences

def preprocess_sentences(sentences: List[TextBlob]) -> List[List[TextBlob]]:
    """Clean up text for summarization."""

if __name__ == '__main__':
    print(summarize('hello dude'))