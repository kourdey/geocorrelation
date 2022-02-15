import streamlit as st
import pandas as pd
#import numpy as np
import altair as alt
import math
import matplotlib.pyplot as plt
import statistics
from streamlit_tags import st_tags
import geotables


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
            Phi.values["PI"] = 180/math.pi* math.asin(0.8 - 0.094 * math.log10(PI))
            #Phi.values.insert(1,math.asin(0.8 - 0.094 * math.log(PI)))
        print (Phi.values)


class cohesion:
    values = {}
    direct_values = []
    Pa = 100.2
    def __init__(self,N60, PI):
        self.N60 = N60
        self.PI = PI
    
    def correlation(self, N60 = 999, PI = 999):
        #if N60 != 999:
            #cohesion.values["N60"] = 5.51 * N60
            
        if PI != 999 and N60 !=999:
            cohesion.values["PI, N60"] = geotables.alfa(PI)* N60 * cohesion.Pa
            print(cohesion.values)
    
    def correlation_N60(self, N60 = 999, PI = 999):
        if N60 != 999:
            cohesion.values["N60"] = 5.51 * N60
            
        

selectparameter = st.sidebar.selectbox('Select Parameter', ['Phi','Undrained_Cohesion'])
selectModel = st.sidebar.selectbox('Select Constitutive Model', ['Mohr Columb','Hoek Brown'])


if selectparameter == 'Phi':
    placeholder = st.empty()
    
    
    option1 = 0
    option2  = 0
    option3  = 0
    N60 = 999
    PI = 999
    mapping={}
    b = []
    
    if st.checkbox('Direct Values'):
        option3 = 1
        DirectValues = st_tags(label='', text='Press enter to add more')
        
        
        for i in range(len(DirectValues)):
            b.append('S'+str(i))
        
        mapping = dict(zip(b,list(map(float, DirectValues))))
        
        
        st.write(mapping)
        
        
    if st.checkbox('SPT Test - N60'):
        st.markdown('Sandy soil (Reference:**AI-Hashemi 2016**.)')
        N60 = st.number_input("Enter N60", key=0, min_value=0, max_value=100)
        option1 = 1
        
    if st.checkbox('PI'):
        st.markdown('Fine-grained cohesive soil (Reference:**Knlhawy and Mayne, 1990**.)')
        PI = st.number_input("Enter PI", key=1, min_value=0.08, max_value=0.8)
        option2  = 1
        
    
    if option1 !=0 or option2 !=0 or option3 !=0:
        Phi1 = Phi(N60,PI)
        Phi1.correlation(N60,PI)
        st.write(Phi.values)
        
        Phi.values.update(mapping) #Merging dictionnaries
        #names2 = list(mapping.keys())
        names1 = list(Phi.values.keys())
        values1 = list(Phi.values.values())
        #values2 = list(mapping.values())
        #plt.scatter(names1, values1)
        plt.scatter(names1,values1,c="red")
        
        plt.xlabel("Parameter/Sample")
        plt.ylabel("Value")
        plt.title("Simple Scatter Plot")
        plt.show()
             
        st.pyplot(plt)
        
        
        st.write(":heavy_minus_sign:" * 34)
        st.write("Information")
        st.write('Mean Value: ' + str(statistics.mean(list(Phi.values.values()))))
        st.write('Median Value: ' + str(statistics.median(list(Phi.values.values()))))
        st.write('Median High Value: ' + str(statistics.median_high(list(Phi.values.values()))))
        st.write('Median Low Value: ' + str(statistics.median_low(list(Phi.values.values()))))
        st.write('Standard Deviation Value: ' + str(statistics.pstdev(list(Phi.values.values()))))
        
elif selectparameter == 'Undrained_Cohesion':
    placeholder = st.empty()
    option1 = 0
    option2  = 0
    option3  = 0
    N60 = 999
    PI = 999
    mapping={}
    b = []
    cohesion1 = cohesion(N60,PI)
    if st.checkbox('Direct Values'):
        option3 = 1
        DirectValues = st_tags(label='', text='Press enter to add more')
        for i in range(len(DirectValues)):
            b.append('S'+str(i))
        mapping = dict(zip(b,list(map(float, DirectValues))))
        st.write(mapping)
        
    if st.checkbox('N60'):
        st.markdown('Fine-grained cohesive soil (Reference:**Knlhawy and Mayne, 1990**.)')
        N60 = st.number_input("Enter N60", key=0, min_value=0, max_value=100)
        option1  = 1
        cohesion1.correlation_N60(N60,PI)  
        
    if st.checkbox('PI, N60'):
        st.markdown('SPT Test: (Reference:**AI-Hashemi 2016**.)')
        st.markdown('SPT Test & Plasticity Index: Clay soil (Reference:**Stroud, 1975**.)')
        N60 = st.number_input("Enter N60", key=1, min_value=0, max_value=100)
        PI = st.number_input("Enter PI", key=2, min_value=8, max_value=70)
        print(N60)
        print(PI)
        option2  = 1
        cohesion1.correlation(N60,PI)
    
    if option1 !=0 or option2 !=0 or option3 !=0:
        
        st.write(cohesion.values)
        
        cohesion.values.update(mapping) #Merging dictionnaries
        
        names1 = list(cohesion.values.keys())
        values1 = list(cohesion.values.values())
        
        plt.scatter(names1,values1,c="red")
        
        plt.xlabel("Parameter/Sample")
        plt.ylabel("Value")
        plt.title("Simple Scatter Plot")
        plt.show()
        st.pyplot(plt)
        
        st.write(":heavy_minus_sign:" * 34)
        st.write("Information")
        st.write('Mean Value: ' + str(statistics.mean(list(cohesion.values.values()))))
        st.write('Median Value: ' + str(statistics.median(list(cohesion.values.values()))))
        st.write('Median High Value: ' + str(statistics.median_high(list(cohesion.values.values()))))
        st.write('Median Low Value: ' + str(statistics.median_low(list(cohesion.values.values()))))
        st.write('Standard Deviation Value: ' + str(statistics.pstdev(list(cohesion.values.values()))))
        
