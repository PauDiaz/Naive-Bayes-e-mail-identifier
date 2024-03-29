#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def email_identifier():
	clf=GaussianNB()
	
	# Set the classifier training and count the time to train it (the classifier)
	t0 = time() 
	clf.fit(features_train,labels_train)
	print "Training time:", round(time()-t0, 3), "s" # Time to train the classifier
	
	# Set the prediction module and count the time it takes to make predictions
	t1 = time() 
	pred=clf.predict(features_test) 
	print "Predicting time:", round(time()-t1, 3), "s" # Time to make predictions
	
	# Set the accuracy of the algorithm and print it
	accuracy= round(accuracy_score(labels_test, pred),4)
	print "The accuracy score is:",accuracy

email_identifier()

#########################################################



