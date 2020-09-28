from nltk import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def tokenize(question):
    return sent_tokenize(question)

def getMaxSimilarity(question, question_list):
    questions = [question.question_text for question in question_list]
    if question in questions:
        index = question_list.get(question_text=question)
        return index

    questions.append(question)
    vectorizer = TfidfVectorizer(norm=None)
    X = vectorizer.fit_transform(questions)
    vals = cosine_similarity(X[-1],X)
    np.delete(vals,-1)
    max_value = 0
    index = None
    for val in vals.flat:
        i = list(vals.flat).index(val)
        if max_value < val and question != questions[i]:
            max_value = val
            index = i
    return question_list.get(question_text=questions[index])





# sentences = ["This is the first document", "This document is the second document"]
# vectorizer = TfidfVectorizer(norm=None)
# X = vectorizer.fit_transform(sentences)
# print(cosine_similarity(X[0:1],X).shape)
# print(cosine_similarity(X[0:1],X))

# # This is the perfect to sort out according to similarity
# sentences = ["This is the first document", "This document is the second document","The is the first document"]
# sentence = "This document is the second document"
# if sentence in sentences:
#     print(sentences.index(sentence))
    
# sentences.append(sentence)
# vectorizer = TfidfVectorizer(norm=None)
# X = vectorizer.fit_transform(sentences)
# vals = cosine_similarity(X[-1],X)
# max_value = 0
# index = None
# for val in vals.flat:
#     i = list(vals.flat).index(val)
#     if max_value < val and sentence != sentences[i]:
#         max_value = val
#         index = i
#         print(str() + str(val))
# print(sentences[index])
# print(max_value)