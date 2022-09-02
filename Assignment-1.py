#!/usr/bin/env python
# coding: utf-8

# In[148]:


#Question 1
#List for 10 student ages
ages = [19,22,19,24,20,25,26,24,25,24]

#Sorting list by using sort()
ages.sort()
print(ages)

#Finding min and max
n = min(ages)
m = max(ages)
print('min=',n,', max=',m)

#adding min and max ages to the list
#Using append() to add the values into the list
ages.append(n)
ages.append(m)
print(ages)

#finding median
a = len(ages)
if a%2 == 0:
    median = (ages[a//2] + ages[a//2-1])/2
else:
    median = ages[n//2]
print('Median Age=', median)

# Finding the avgerage age
s = sum(ages)
a = len(ages)
avg = s/a
print('Average Age=',avg)

#Finding range of the ages
range_ages = m-n
print('Range of the ages=',range_ages)
print(len(ages))


# In[ ]:


j= 10
p = 10//3
print(p)


# In[149]:


#Question 2
#Creating a dictionary
dog = {}
#adding keys and values
dog.update({"name":"Snoopy", "color":"white", "breed":"samoyed", "legs":"short", "age":"17"})
print(dog,'\n')

#creating a student dictionary
std = {
    "first_name":"Ishyanth",
    "last_name":"Kadali",
    "gender":"male",
    "age":"23",
    "martial_status":"Single",
    "skills":["python", "tensorflow", "keras", "pandas"],
    "country":"USA",
    "city":"Warrensburg",
    "Address":"501 Joll St"
    }
print(std,'\n')
#finding Lenght of dictionary
print(len(std),'\n')

#type check
v = std.get("skills")
print(v)
print(type(v),'\n')

#Modifying values
std["skills"].append("java")
std["skills"].append("C++")
print(std,'\n')

#Dictionary keys as list
print(std.keys(),'\n')
#Dictionary values as list
print(std.values())


# In[62]:


#Question 3
#creating tuples
brothers = ('Phani','Deep','Karthik','Chintu')
sisters = ('Vinela','Hanisha', 'Bharani')
#join tuples
siblings = brothers + sisters
print(siblings)
#lenght of tuples
print('Number of siblings =',len(siblings),'\n')

#we can't modify tuples
parents = ('Lakshmana Rao','Satya Veni')
family_members = siblings + parents
print(family_members)


# In[63]:


#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Finding the length of it_companies
print("length of it_companies:", len(it_companies))
it_companies.add('Twitter')
print(it_companies)

#adding companies
it_companies.update(['Tesla','Razer','Alienware'])
print(it_companies)

#removing a company
it_companies.remove('IBM')
print(it_companies)

'''Difference between remove and discard is if the item doesn't exist, the remove() function
   will raise an error, but the discard() method won't.'''

#joining 2 sets
C = A.union(B)
print(C)

#Intersection
D = A.intersection(B)
print(D)

#Subset
E = A.issubset(B)
print(E)

#Disjoint sets
F = A.isdisjoint(B)
print(F)

#Joining sets
A.update(B)
print(A,'\n')
B.update(A)
print(B,'\n')

#Symmetric Diff
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
G = A.symmetric_difference(B)
print('symmetric_difference A nad B is', G)

#Deleiting the sets
A.clear()
B.clear()
print(A)
print(B)

#Coverting ages to set
age_set = set(age)
print(age_set)

#compare
x = len(age)
z = len(age_set)
print("Length of the list is greater than length of the set:", x>z)


# In[64]:


#Question 5
# calculating radius and circumference of a circle
r = 30
print('radius of a circle', r)
_area_of_circle_ = 3.14*r**2
_circum_of_circle_ = 2*3.14*r
print('Area of the circle',_area_of_circle_)
print('Circumference of the circle',_circum_of_circle_, '\n')

#New radius input
radius = float(input('enter the new radius of the circle = '))

_area_of_circle_ = 3.14*radius**2

print('Area of the circle',_area_of_circle_)


# In[65]:


#Question 6
sen= "I am a teacher and I love to inspire and teach people"

#By using split methods and set

words=set(sen.split(' '))

#finding No. of unique words
print('Number of Unique words = ',len(words))

print('Unique Words in the sentence are ')
for w in words:
    print(w)


# In[66]:


#Question 7
#tab escape sequence
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t250\tFinland\t\tHelsinki')


# In[67]:


#Question 8
#string formatting method
radius = 10
area = 3.14*radius**2
print("The area of a circle with radius ",radius," is ",int(area)," meters suqare.")


# In[68]:


#Question 9
#Reading input from user
n = int(input('Enter the number of students: '))
lbs = []
kg = []
for i in range(0,n):
    t = float(input('Enter the weight: '))
    lbs.append(t)

#concerting lbs to kgs
ki = 0.45359237
for y in lbs:
    kg.append(y * ki)
print(kg)


# In[38]:


#Question 10
#importing libraries
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler    
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import confusion_matrix  


# In[39]:


#reading the dataset
dataset=pd.read_csv("dataset.csv")
print(dataset)
X= dataset['f'].values  
y= dataset['output'].values 


# In[40]:


#using reshape to convert data into 2 dimensional array
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size = 0.5)
X_train = np.array(X_train).reshape(-1,1)
X_test = np.array(X_test).reshape(-1,1)


# In[41]:


#Data normalization
norm= StandardScaler()  
X_train= norm.fit_transform(X_train)    
X_test= norm.transform(X_test)  


# In[42]:


#creating KNN model
model= KNeighborsClassifier(n_neighbors=3, metric= 'euclidean' )  
#Data fitting into the model
model.fit(X_train, y_train)


# In[57]:


#Predicting the test set result  
predict_output = model.predict(X_test) 
print(X_test)
thresults = []
for i in X_test:
    if i < 1.5:
        thresults.append('cross')
    else:
        thresults.append('dot')
print("Output:",thresults)


# In[69]:


#checking the output by confusion matrix
results= confusion_matrix(y_test, thresults) 
print("Confusion matrix:\n",results)


# In[70]:


#finding model accuracy
count=sum(sum(results))
accuracy=(results[0,0]+results[1,1])/count
print ('Accuracy=', accuracy)


# In[71]:


# finding model sensitivity
sense = results[0,0]/(results[0,0]+results[0,1])
print('Sensitivity=', sense )


# In[72]:


#finding model specificity
specificity = results[1,1]/(results[1,0]+results[1,1])
print('Specificity=', specificity)

