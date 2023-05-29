import pandas as pd 
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=200, n_features=2, n_informative=1,n_redundant=0,
                           n_classes=2, n_clusters_per_class=1, random_state=41,hypercube=False,class_sep=10)
df = pd.DataFrame(X  ,  y )
df.to_csv("datasets.csv")