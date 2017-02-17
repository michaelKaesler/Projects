# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 19:06:01 2016

@author: mkaesler

This is just a prototype of the sentiment analysis for lincoln park zoo comments.

"""

import pandas as pd
import nltk


def read_data(train_data, real_data):
    # train_data and real_data are the file paths for the two 
    # reading both into a pandas df 
    trainDF = pd.read_table(train_data, sep = '\t')
    realDF = pd.read_csv(real_data)
    
    # first have to add positive/negative based off one's and zeros
    pos_list = []
    for index, rows in trainDF.iterrows():
        if rows['label'] == 1:
            pos_list.append('positive')
        else:
            pos_list.append('negative')
    trainDF['label_word'] = pos_list
    
    # getting tuples of tweet and sentiment for just training data
    training_list = []
    for index, rows in trainDF.iterrows():
        body_label = (rows['body'], rows['label_word'])
        training_list.append(body_label)
    
    # print training_list                         ######## training tuple is ok
    
    # creating filtered training list
    # getting rid of words with less than two letters and making rest lowercase
    training_list_filtered = []
    for (words, sentiment) in training_list:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        filtered_tuple = (words_filtered, sentiment)
        training_list_filtered.append(filtered_tuple)
        
    # print training_list_filtered       ############## filtered tuple is gravy
        
    
    
    return trainDF, realDF, training_list_filtered 
    
def get_words_in_data(training_list):
    all_words = []
    for (words, sentiment) in training_list:
        all_words.extend(words)
    return all_words
    
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
    
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
    
    
    
def train_classifier(extract_features, training_list, word_features):
    training_set = nltk.classify.apply_features(extract_features, training_list)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier
    
def classify_comments(classifier, realDF, word_features):
    # extract the comments from the realDF (later on can do things with the id's here)
    # first need to make sure the column is only strings (otherwise wont run)
    realDF['comment_body'] = realDF['comment_body'].astype(str)

    comments = []
    for index, rows in realDF.iterrows():
        comments.append(rows['comment_body'])
        
    # create dataframe of comments and classification by the conjoining of two lists
    labels = []
    for i in comments:
        label = classifier.classify(extract_features(i.split()))
        labels.append(label)
    
    realDF['labels'] = labels
    print realDF.head(5)
    
    realDF.to_csv('labeled_comments.csv')
    
    
    return None
    

if __name__ == '__main__':
    trainDF, realDF, training_list = read_data('UMICHtrain.txt', 'fb_comments.csv')    
    word_features = get_word_features(get_words_in_data(training_list))    
    classifier = train_classifier(extract_features, training_list, word_features)
    classify_comments(classifier, realDF, word_features)
    
    # tweet = 'Larry is my friend'
    # print classifier.classify(extract_features(tweet.split()))
    
    
    
    
    
    
    
    
    
    
    
    