# Machine-Learning-CS5710
Assignment-1
CS-5710
CRN: 11813

Video link: https://drive.google.com/drive/folders/1RLHZ5lY0HByWKbaFn29dUVo3ajMKOHIO?usp=sharing

Modifying Lists, Sets, Tuples, Dictionaries
Question 1
Created a list of 10 students ages.
• Sorting the list by using sort() method .
and finding the min and max age by using min() and max() methods.
• By using append() the min age and the max age are added to the list. Basically append() adds values to the list at last
• Finding the median age by using floor division // operator we can find index of the list to calculate median.
• Average is sum of all the values of the list using sum() method divided by length of the list by using len() method.
• Already we have max and min values, so max- min gives range of the ages.

Question 2
• Created an empty dictionary called dog and added name, color, breed, legs, age to the dog dictionary
• Created a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.
• By using len() method to find length of the student dictionary.
• By using get(), printing the value of skills and checking the data type with type() method.
• Modify the skills values by appending to the skills key .
• Using keys() we can print all the keys in the dictionary.
• Using values() we can print all the values in the dictionary.

Question 3
• Created 2 tuples containing names of sisters and brothers.
• Joined brothers and sisters tuples by using + operator and assigned it to siblings.
• Used len() method to find out the length of the tuple.
• We can’t modify the siblings tuple. So I created a parents tuple with name of father and mother and assign it to family_members by joining siblings and parents tuples.

Question 4
• len() to find the length of the set it_companies
• Added 'Twitter' to it_companies by append() method.
• Inserted multiple IT companies at once to the set it_companies by appending values in list format.
• Removed one of the companies from the set it_companies using remove() function.
• Difference between remove and discard is if the item doesn't exist, the remove() function will raise an error, but the discard() method won't.
• Joining A and B using union()
• By using intersection() we can find A intersection B
• We can know A subset of B or not by issubset().
• We can know A and B disjoint sets or not by using isdisjoint().
• Using update() method joined A with B and B with A.
• Common values by using symmetric difference between A and B
• Clear() deletes the sets completely.
• By converting the ages to a set, it removes the duplicated and comparing the length of the list and the set will results list is greater than set as there are no duplicates in set.

Question 5
Radius = 30 meters.
Using ** operator for calculating exponential values
• Took the input radius from user and calculated the area.

Question 6
“I am a teacher and I love to inspire and teach people”
There are 10 unique words in the sentence.
By split methods and set we can produce unique words.

Question 7
By using tab escape sequence

Question 8
By using string formatting method
Variables and sentences can be displayed in one print statement.

Question 9
Python program, which reads weights (lbs.) of N students into a list and convert the weights to kilograms in a separate list using for Loop.

Question 10
• Importing libraries which are numpy to work with arrays, pandas to import and feed the dataset to the model.
• Importing scikit learn to work with KNN classifier and confusion matrix and to split the data into test data and training data.
• Using reshape() method to convert data into 2 dimensional array.
• Split the data into 50:50 ratio.
• Using StandardScaler()to normalize the data.
• Creating a K Nearest Neighbor classifier to predict the output.
• Giving the k=3 to KNN model.
• Fitting the data into the model to train.
• Predicting the test set result by giving test data.
• Put a threshold if the values in X_test less than 1.5 then it will be classified as cross or else dot.
• Checking the predicted results by using confusion matrix.
• Here, we got 2 true positives and 2 true negatives.
• The model got 100% accuracy.
• The model got 100% sensitivity as it is correctly predicting positives instances.
• The model got 100% specificity as it is correctly predicting negative instances.
Video link: https://drive.google.com/drive/folders/1RLHZ5lY0HByWKbaFn29dUVo3ajMKOHIO?usp=sharing
