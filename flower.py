import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

st.title('Machine Learning Demo')

st.write("""
# Explore different classifiers and datasets
""")

dataset_name = st.sidebar.selectbox(
  'Select Dataset',
  ('Iris', 'Breast Cancer', 'Wine')
)

st.write(f"## {dataset_name} Dataset")

classifier_name = st.sidebar.selectbox(
  'Select classifier', 
  ('K Nearest Neighbor', 'Support Vector Machine', 'Random Forest')
)


def get_dataset(name):
  data = None
  if name == 'Iris':
    data = datasets.load_iris()
  elif name == 'Wine':
    data = datasets.load_wine()
  else:
    data = datasets.load_breast_cancer()
  X = data.data
  y= data.target
  return X, y, data


X, y,data = get_dataset(dataset_name)
st.write('Shape of dataset:', X.shape)
st. write('Number of classes:', len(np.unique(y)))

def get_classifier(clf_name, params):
  clf = None
  if clf_name == 'Support Vector Machine':
    clf = SVC(C=params['C'])
  elif clf_name == 'K Nearest Neighbor':
    clf = KNeighborsClassifier(n_neighbors=params['K'])
  else:
    clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'],
        max_depth=params['max_depth'], random_state=1234)
  return clf

def add_parameter_ui(clf_name):
  params = dict()
  if clf_name == 'Support Vector Machine':
    C = st.sidebar.slider('C', 0.01, 10.0)
    params['C'] = C
  elif clf_name == 'K Nearest Neighbor':
    K = st.sidebar.slider('K', 1, 15)
    params['K'] = K
  else:
    max_depth = st.sidebar.slider('max_depth', 2, 15)
    params['max_depth'] = max_depth
    n_estimators = st.sidebar.slider('n_estimators', 1, 100)
    params['n_estimators'] = n_estimators
  return params

params = add_parameter_ui(classifier_name)

clf = get_classifier(classifier_name, params)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)

st.write(f'Classifier = {classifier_name}')
st.write(f'Accuracy =', acc)

pca = PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1] 

fig = plt.figure()
plt.scatter(x1, x2,
            c=y, alpha=0.8,
            cmap='viridis')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

st.pyplot(fig)

st.write(f'{dataset_name} Dataset')
if dataset_name == 'Iris':
    data1 = datasets.load_iris(as_frame=True)
elif dataset_name == 'Wine':
    data1 = datasets.load_wine(as_frame=True)
else:
    data1 = datasets.load_breast_cancer(as_frame=True)
st.dataframe(data1.data)

