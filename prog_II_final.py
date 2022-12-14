import numpy as np
import pandas as pd
import streamlit as st

 educ = st.selectbox("Education level", 
              options = ["High School Diploma",
                         "College Degree",
                         "Graduate Degree"])
 st.write(f"Education (pre-conversion): {educ}")
 st.write("**Convert Selection to Numeric Value**")
 if educ == "High School Diploma":
     educ = 1
 elif educ == "College Degree":
     educ = 2
 else:
     educ = 3
    
 st.write(f"Education (post-conversion): {educ}")