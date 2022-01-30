import streamlit as st
import pandas as pd
#import numpy as np
import altair as alt
import math
import matplotlib.pyplot as plt

class Phi:
    values = {}
    direct_values = []
    
    def __init__(self,N60, PI):
        self.N60 = N60
        self.PI = PI
    
    def correlation(self,N60 = 999, PI = 999):
        if N60 != 999:
            Phi.values["N60"] = 26.232 + 0.408*N60 - 0.002*N60**2 + (9.966*10**(-6)) * N60**3
            #Phi.values.insert(0,26.232 + 0.408*N60 - 0.002*N60**2 + (9.966*10**(-6)) * N60**3)
        if PI != 999:
            Phi.values["PI"] = math.asin(0.8 - 0.094 * math.log(PI))
            #Phi.values.insert(1,math.asin(0.8 - 0.094 * math.log(PI)))
        print (Phi.values)


if st.sidebar.selectbox('Select', ['Phi','c','E'],key =1) == 'Phi':
    option1 = 0
    option2  = 0
    N60 = 999
    PI = 999
    if st.checkbox('SPT Test - N60'):
        st.markdown('Sandy soil (Reference:**AI-Hashemi 2016**.)')
        N60 = st.number_input("Enter N60", key=0, min_value=0, max_value=100)
        option1 = 1
    if st.checkbox('PI'):
        st.markdown('Fine-grained cohesive soil (Reference:**Knlhawy and Mayne 1990**.)')
        PI = st.number_input("Enter PI", key=1, min_value=8, max_value=20)
        option2  = 1
    
    if option1 !=0 or option2 !=0:
        Phi1 = Phi(N60,PI)
        Phi1.correlation(N60,PI)
        st.write(Phi.values)
        #pd.DataFrame.from_dict(Phi.values)
        #df = pd.DataFrame.from_records(Phi.values)
        #df = pd.DataFrame(Phi.values)
        names1 = list(Phi.values.keys())
        values1 = list(Phi.values.values())
        #plt.bar(range(len(Phi.values)), values, tick_label=names)
        plt.scatter(names1, values1)
        #plt.show()
        st.pyplot(plt)
elif st.sidebar.selectbox('Select', ['Phi','c','E'], key = 2) == 'E':
    print("2")
    






        
        
        






