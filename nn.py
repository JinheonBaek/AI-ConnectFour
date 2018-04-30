import pickle
import pandas as pd

data = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data = pd.DataFrame(data = data).T

width = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
height = range(1, 7)
cols = []

for i in width:
    for j in height:
        cols.append(i + str(j))
data.columns = cols

MLP_classifier = pickle.load(open('model/MLP.data', 'rb'))
predict = MLP_classifier.predict_proba(data)
print(predict[0][2] - predict[0][0])