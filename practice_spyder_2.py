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
"""These are all the basic scientific libraries used to run such highly Computational Algo's"""

#Importing the Datasets:
datasets = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
"""Importing the Datasets for market_research by eliminating the Header over it, as it was coying the different items 
in the list as the header for the file"""

#Forming the Pre-Model of Apriori:
transaction  = []
for i in range(0,7501): #Running for every basket of data
    transaction.append([str(datasets.values[i,j]) for j in range(0,20)]) #String list of the items in the basket   
"""Running the multi-loop simultaneously for the purpose of converting the items for every basket into the string list 
of the items within the basket for a certain customer""". 

#Training of the Model:
from apyori import apriori #importing the Apriori Library
rules = apriori(transaction,min_support = 0.005, min_confidence = 0.2, min_lift = 4, min_length = 3) #Creating Notable threshold in basket
"""Providing the minimum value of support, confidence and lift to separate-out possible basket items
relating to eachother in percentage value among the entire list for item-pair mining"""

#Forming the Set of Values Matrix:
results = list(rules) #Creating the list from Frozenset of Close Association Obtained from Data
asso_list=[]          #List of the Associated items only
asso_support = []     #Array of respective support values.
asso_joiner = []  
asso_confidence = []  #Array of respective confidence values
asso_lift = []        #Array of respective lift values

for i in range(0, len(results)):
    asso_list.append([str(results[i][0])])  #Items should be in list. Otherwise it will be in frozen(Unviewable) State
    asso_support.append(results[i][1])      #It will append all the min_support value for the pair of Association
"""Forming the list array of the values of the Items list and the support values"""
    
for i in range(0, len(results)):
    asso_joiner = results[i][2]                # A separet list was created to store the confidence and value as they were not accessible from
                                               # "resuts" list.
    asso_confidence.append(asso_joiner[0][2])  #It will append all the min_confidence value for the pair of Association
    asso_lift.append(asso_joiner[0][3])        #It will append all the min_lift value for the pair of Association   
    
#Visualizing the Results:

#Currently, I have done this very basic kind of visualiztion which needs to be more elaborate and extensive. yet it is clear and concise.
#Suggestion are welcomed on better visualization methods

#Plotting the Scatter Plots for the Association Results(Between Support and Confidence Value):
plt.scatter(range(1, 9), asso_support,  c = 'blue', label = 'Support Level(in %)')
plt.scatter(range(1, 9), asso_confidence,  c = 'red', label = 'Confidence Level(in %)')
plt.title('Apriori Params')
plt.xlabel('Associations in Order')
plt.ylabel('% Value')
plt.legend()
plt.show()

#Plotting the Bar Plots for the Association Results(Between the Results Index and Support and Confidence Values):
plt.bar(range(1,9), asso_support)
plt.bar(range(1,9), asso_confidence)
plt.title('Apriori Params')
plt.xlabel('Associations in Order')
plt.ylabel(' Confidence (in% Value)')
plt.legend()
plt.show()




  
    
    
