# The-Apriori-Mall
"""It will be a Apriori Model based project for better Visualization of the Customer Purchasing Pattern"""
"""The model is being analyzed on the Python framewok, simply because of it's user-friendly scripting and favorably higher availability of the Data Analyzing Libraries"""
#Important terms required for Association Models:
#Minimum Support Vectors:
 It represents the ratio of the consumption of one particular object, service, product over the entire sampling available.
 
 Min. Support  = One particular(Object,Product, Service) / Entire Dataset Rounds
 
 #Minimum Confidence Vectors:
 It represents the close knit association of the consumtion of another thinng/product/service w.r.to the previous one.
  
 Min. Confidence = (Movie 2 watched w.r.to Movie 1)/ Instances of Movie 2 only from Samples

#Minimum Lift Ratio:
 It is the ratio of the Minimum Confidence to the Minimum Support which is a floating term and represents the association fractional level of the different items.
 
 #Buiding an Apriori Modedl of Association in Python:
 
 #Importing the Libraries:
 import numpy as np
 import pandas as pd
 import matplotlib.pyplot as plt
 
 #Importing the Datasets:
 datasets = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
 
 #Pre-Modelling of the Apriori Model:
 for i in range(0,7501):
     transaction.append([str(datasets.values[i,j]) for j in range(0,20)])
    
 #Implementing the Apriori Model:
 from spyori import apriori
 rules = apriori(transaction, min_support = 0.003, min_confidence = 0.05, min_lift = 3, min_length = 2)
 
 

