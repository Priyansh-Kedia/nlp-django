from nltk import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def tokenize(question):
    return sent_tokenize(question)

def getMaxSimilarity(question, question_list):
    sentences = ["This is the first document", "This document is the second document","The is the first document"]
    sentence = "This document is the second document"
    questions = [question.question_text for question in question_list]
    if question in questions:
        index = question_list.get(question_text=question)
        print(index.answer_text)
        return question

    questions.append(question)
    print(questions)
    vectorizer = TfidfVectorizer(norm=None)
    X = vectorizer.fit_transform(questions)
    print(cosine_similarity(X[-1],X))
    vals = cosine_similarity(X[-1],X)
    np.delete(vals,-1)
    print([val for val in vals.flat])
    max_value = 0
    index = None
    for val in vals.flat:
        i = list(vals.flat).index(val)
        if max_value < val and question != questions[i]:
            max_value = val
            index = i
    print(questions[index])
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