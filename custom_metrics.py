from autogluon.core.metrics import make_scorer, Scorer
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.metrics import f1_score

classes = [0, 1, 2, 3, 4, 5, 6]
weights = np.array([0.0385, 0.0328, 0.2791, 0.1812, 0.0113, 0.2952, 0.1614])

def competition_metric(y_true, y_pred):
    score = np.sum(f1_score(y_true, y_pred, average=None, labels=classes) * weights)
    return score

# Autogluon'un kendi make_scorer fonksiyonunu kullanarak scorer oluşturulması
weighted_f1_scorer = make_scorer(name='custom_weighted_f1',
                                 score_func=competition_metric,
                                 optimum=1,
                                 greater_is_better=True)