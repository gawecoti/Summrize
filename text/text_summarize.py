# Text summarization based on H.P Luhn's approach from "The Automatic Creation of Literature Abstracts"
# Code from Matthew Russell (re-wrote certain sections) - http://nbviewer.ipython.org/urls/raw.github.com/ptwobrussell/Mining-the-Social-Web-2nd-Edition/master/ipynb/Chapter%205%20-%20Mining%20Web%20Pages.ipynb

import nltk
import json
import numpy as np

MAX_INDEX_DIST = 5
TOP_SENTENCES = 5

def score_sentences (sentences, important_words):
    sentence_scores = []
    sentence_index = -1

    # Identify important words in each sentence
    for sentence in sentences:
        sentence_index += 1
        word_index = []
        sentence_tokenize = nltk.tokenize.word_tokenize(sentence)

        for word in sentence_tokenize:
            if word in important_words:
                word_index.append(sentence_tokenize.index(word))

        if len(word_index) == 0:
            continue

        # Form clusters in the sentence
        word_index.sort()

        cumulative_cluster = []
        current_cluster = [word_index[0]]
        i = 1

        while i < len(word_index):
            if word_index[i] - word_index[i-1] < MAX_INDEX_DIST:
                current_cluster.append(word_index[i])
            else:
                cumulative_cluster.append(current_cluster)
                current_cluster = [word_index[i]]
            i += 1

        cumulative_cluster.append(current_cluster)

        # Give scores for each sentence using equation (number of clusters)^2/total number of words in cluster
        MAX_CLUSTER_SCORE = 0

        for cluster in cumulative_cluster:
            important_words_cluster = len(cluster)
            num_words_cluster = cluster[-1] - cluster[0] + 1
            score = (important_words_cluster*important_words_cluster)/(num_words_cluster) * 1.0

            if score > MAX_CLUSTER_SCORE:
                MAX_CLUSTER_SCORE = score

        sentence_scores.append((sentence_index, MAX_CLUSTER_SCORE))

    return sentence_scores

def summarize(text):
    text_data = text
    important_words = []

    # Get important words
    sentences = nltk.tokenize.sent_tokenize(text_data)

    for sentence in sentences:
        for word in nltk.tokenize.word_tokenize(sentence):
            if word.lower() not in nltk.corpus.stopwords.words("english")[:100]:
                important_words.append(word.lower())

    # Score each sentence
    sentence_scores = score_sentences(sentences, important_words)

    # Calculate top scores

    # Average method
    average = np.mean([s[1] for s in sentence_scores])
    stdev = np.std([s[1] for s in sentence_scores])
    mean_score_sentences = []

    for (sentence_index, sentence_score) in sentence_scores:
        if sentence_score > 0.5 * stdev + average:
            mean_score_sentences.append(sentence_index)

    # Top score method
    top_n_scored = sorted(sentence_scores, key=lambda s: s[1])[-TOP_SENTENCES:]
    top_n_scored = sorted(top_n_scored, key=lambda s: s[0])

    # Print results
    summarized_sentences_mean = ''
    summarized_sentences_top = ''

    for sentence_index in mean_score_sentences:
        summarized_sentences_mean += sentences[sentence_index]

    for sentence_index in top_n_scored:
        summarized_sentences_top += sentences[sentence_index[0]]

    return ((summarized_sentences_mean, summarized_sentences_top))

