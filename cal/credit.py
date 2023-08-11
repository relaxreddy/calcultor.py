import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data = pd.read_csv(r"C:\Users\RELAX REDDY\Desktop\python_ws\creditcard.csv")
data.head()