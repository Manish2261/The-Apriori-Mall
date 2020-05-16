# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:18:23 2020

@author: Lenovo
"""

#Apriori Model for Item Clustering

#Importing the Library:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the Datasets:
datasets = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

#Forming the Pre-Model of Apriori:
transaction  = []
for i in range(0,7501):
    transaction.append([str(datasets.values[i,j]) for j in range(0,20)])   

#Training of the Model:
from apyori import apriori
rules = apriori(transaction,min_support = 0.005, min_confidence = 0.2, min_lift = 4, min_length = 3)

#Forming the Set of Values Matrix:
results = list(rules)
asso_list=[]
asso_support = []
asso_joiner = []
asso_confidence = []
asso_lift = []

for i in range(0, len(results)):
    asso_list.append([str(results[i][0])]) #Otherwise it will be in frozen(Unviewable) State
    asso_support.append(results[i][1]) #It will append all the min_support value for the pair of Association

for i in range(0, len(results)):
    asso_joiner = results[i][2]      
    asso_confidence.append(asso_joiner[0][2])#It will append all the min_confidence value for the pair of Association
    asso_lift.append(asso_joiner[0][3]) #It will append all the min_lift value for the pair of Association   
    
#Visualizing the Results:
    
#Plotting the Scatter Plots for the Association Results
"""plt.scatter(range(1, 9), asso_support,  c = 'blue', label = 'Support Level(in %)')
plt.scatter(range(1, 9), asso_confidence,  c = 'red', label = 'Confidence Level(in %)')
#plt.scatter(range(1, 9), asso_lift, s = 40, c = 'magenta', label = 'Min_Lift')
plt.title('Apriori Params')
plt.xlabel('Associations in Order')
plt.ylabel('% Value')
plt.legend()
plt.show()
"""
#Plotting the Bar Plots for the Association Results
plt.bar(range(1,9), asso_support)
plt.bar(range(1,9), asso_confidence)
plt.title('Apriori Params')
plt.xlabel('Associations in Order')
plt.ylabel(' Confidence (in% Value)')
plt.legend()
plt.show()



  
    
    
