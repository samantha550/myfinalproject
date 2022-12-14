import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


s = pd.read_csv('/Users/samsa/OneDrive/Desktop/Programming II/social_media_usage.csv')
s.ndim

def clean_sm(x):
    x = np.where (x == 1, 1,0)
    return x

ss = pd.DataFrame({
    "sm_li": clean_sm(s["web1h"]),
    "income": np.where(s["income"]>9, np.nan, s["income"]),
    "education": np.where(s["educ2"]>8, np.nan, s["educ2"]),
    "parent": clean_sm(s["par"]),
    "married": clean_sm(s["marital"]),
    "female": np.where(s["gender"] == 2, 1,0),
    "age": np.where(s["age"] > 98, np.nan, s["age"])
    
})

ss = ss.dropna()

y = ss["sm_li"]
x = ss[["age", "education", "parent", "female","income","married"]]

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    stratify = y,
    test_size = 0.2,
    random_state = 987
)

lr = LogisticRegression(class_weight = 'balanced')
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

pd.DataFrame(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

educ = st.selectbox("Education level", 
                    options = ["High School Diploma","College Degree","Graduate Degree"])

st.write(f"Education (pre-conversion): {educ}")
st.write("**Convert Selection to Numeric Value**")
if educ == "High School Diploma":
   educ = 1
elif educ == "College Degree":
     educ = 2
else:
     educ = 3

st.write(f"Education (post-conversion): {educ}")
