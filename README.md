# The-Apriori-Mall
It will be a Apriori Model based project for better Visualization of the Customer Purchasing Pattern

It is one of the models in the area of the Association learning algorithm which provides us with the items which are bought in the combination frequently from the Super-shops. It gives us the value of support, confidence and lift rate of the items which are closely associated relevantly with each other.

If the associated list items with better values are kept in combination within the space, which could result into greater sales per customers visiting the outlet for purchasing.

### Important Definitions:

#Mininum Support:
It is the ratio of item repetition in the entire list of the baskets of the data.
It is expressed in terms of the percentage of the entire order within the basket.

  Minimum Support = Number of Repetition of Order A / Total Number of list rounds.

#Minimum Confidence:
It represents the ratio of the association of another item w.r.to the first item considered above to the entire instances when the second relative item is ordered in the baskets

  Minimum Confidence = Movie 2 watched after watching Movie 1 / Total Movie 2 watching crowd

#Minimum Lift :
It is the ratio of Minimum Confidence to the Minimum Support value.

  Minimum Lift Value = Minimum Confidence / Minimum Support 

Q. Why I needed required a list array of value additionally named as "asso.join[]"?
It is because the list of array of "results" was not feasible to be used for forming another list containing the different values of the Support, Confidence, Lift vectors from the data given.

Q. How to choose for the value of Support, Confidence, Lift variable in defining the Association Model?
It will completely depend upon your customization practice, requirements from the model, size of the data as for every other value of support, confidence, lift we will get different sizes of Association matrix of the different items within the list, and we must visualize the same and should take decision accordingly then.
