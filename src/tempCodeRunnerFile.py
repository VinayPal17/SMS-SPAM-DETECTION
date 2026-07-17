from sklearn.feature_extraction import CountVectorizer

messages = [
    "free offer now",
    "claim free prize",
    "metting tommorow"
]

cv = CountVectorizwer()

X = cv.fit_transfrom(messages)

print(type(X))

print(X.shape)

print(X.vocabulary_)

print(X)

print(X.toarray())