from sklearn.metrics import jaccard_similarity_score

def score(y_true,y_pred):
    y_true = set(y_true)
    y_pred = set(y_pred)
    score = len(y_true&y_pred)/len(y_true|y_pred)
    # score = jaccard_similarity_score(y_true,y_pred)
    return score