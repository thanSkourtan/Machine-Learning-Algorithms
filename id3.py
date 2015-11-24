'''
Created on 24 Nov 2015

@author: thanskourtan
'''


import itertools 

file = [line.split(",") for line in itertools.islice(open("..//Python//heart_train.arff.txt"),16,None)]

print(file)

