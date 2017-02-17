Purpose

-the objective is to take two side by side texts, one correct (the actual state), and the other being the correct state except with typos (the observed state) and create a hidden markov model describing the system. Then the viterbi algorithim is used to find the most likely sequence of hidden states given the observed text (with typos). The HMM is created on a training set of the data, and then tested on the test set. 

to run, just type python viterbiVC4.py

-it will output the outputPART2.txt, which is already included in the folder, 
