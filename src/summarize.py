"""Summarize a body of text."""
import copy
from typing import List, Dict
from collections import defaultdict as ddict

from textblob import TextBlob, Sentence
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

# TODO: EVALUATE STOP WORDS

def summarize(tldr: str) -> List[str]:
    """Summarize a body of text."""
    text = TextBlob(tldr)
    sentences = text.sentences

    preprocessed_sentences = preprocess_sentences(sentences)

    word_scores = score_words_for_significance(preprocessed_sentences)

    sentence_scores = score_sentences(preprocessed_sentences, word_scores)

    # TODO: average scores

    # TODO: Return sentences filtered if sentence_scores[index] >= avg + threshold

    return sentences

def preprocess_sentences(sentences: List[Sentence]) -> List[List[str]]:
    """Clean up text for summarization."""
    # IMPORTANT: Keep in same order!
    sents = []
    for sent in sentences:
        significant_words = [word for word in sent.tokens if word not in stopwords]
        sents.append(significant_words)

    # TODO: Lemmetize, find references...
    
    return sents

def score_words_for_significance(word_lists: List[List[str]]) -> Dict[str, float]:
    """Rate each word in a text for importance (normalized frequency)."""
    counts = ddict(int)
    for word_list in word_lists:
        for word in word_list:
            counts[word] += 1
    
    count_list = [(word, count) for word, count in counts.items()]
    sorted_by_count = sorted(count_list, key=lambda tup: tup[1], reverse=True)
    most_occurrences = sorted_by_count[0][1]
    
    scores = {
        word: score / most_occurrences for word, score in counts.items()
    }

    return scores

def score_sentences(sentences: List[List[str]], word_weights: Dict[str, float]) -> Dict[int, float]:
    """Score sentences in terms of importance (return a dict[index, importance])."""
    scores = {}
    for i, sentence in enumerate(sentences):
        score = sum([word_weights[word] for word in sentence]) / len(sentence)
        scores[i] = score
    
    print(scores)
    quit()

if __name__ == '__main__':
    print(summarize('well a dog is a dog of course. dogs cant argue with horses or dogs or dogs dogs dogs dogs dogs dogs!'))