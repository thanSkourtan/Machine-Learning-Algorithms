
import math

#referrer, country, read FAQ, Pages Viewed, Service chosen

my_data=[['slashdot','USA','yes',18,'None'],
 ['google','France','yes',23,'Premium'],
 ['digg','USA','yes',24,'Basic'],
 ['kiwitobes','France','yes',23,'Basic'],
 ['google','UK','no',21,'Premium'],
 ['(direct)','New Zealand','no',12,'None'],
 ['(direct)','UK','no',21,'Basic'],
 ['google','USA','no',24,'Premium'],
 ['slashdot','France','yes',19,'None'],
 ['digg','USA','no',18,'None'],
 ['google','UK','no',18,'None'],
 ['kiwitobes','UK','no',19,'None'],
 ['digg','New Zealand','yes',12,'Basic'],
 ['slashdot','UK','no',21,'None'],
 ['google','UK','yes',18,'Basic'],
 ['kiwitobes','France','yes',19,'Basic']]


my_data2 = [
           ["Rainy","Hot","High","False","No"],
           ["Rainy","Hot","High","True","No"],
           ["Overcast","Hot","High","False","Yes"],
           ["Sunny","Mild","High","False","Yes"],
           ["Sunny","Cool","Normal","False","Yes"],
           ["Sunny","Cool","Normal","True","No"],
           ["Overcast","Cool","Normal","True","Yes"],
           ["Rainy","Mild","High","False","No"],
           ["Rainy","Cool","Normal","False","Yes"],
           ["Sunny","Mild","Normal","False","Yes"],
           ["Rainy","Mild","Normal","True","Yes"],
           ["Overcast","Mild","High","True","Yes"],
           ["Overcast","Hot","Normal","False","Yes"],
           ["Sunny","Mild","High","True","No"]
]


'''
we assume that we always calculate the entropy of the last attribute 
which is the target function value
target_attribute_values is a dictionary ex.{'No':3, 'Yes':5}. We find the entropy of a set of 3 No and 5 Yes

'''

class Tree:
    
    def __init__(self):
        self.root = self.Node() #create a root node for the tree
        
        
    '''we need to set fields in 3 different nodes. The one to be added, its parent and its left sibling, 
       label and attribute are defined later. 
    '''
    def add_node(self,parent_node,left_sibling_node):
        new_node = self.Node()
        new_node.top = parent_node
        
        
        if parent_node.left_child==None:
            parent_node.left_child = new_node  
        
        if left_sibling_node != None:
            left_sibling_node.right_sibling=new_node
            
        return new_node,parent_node,left_sibling_node
        
    
    class Node():
        def __init__(self,attribute=None,top=None,left_child=None,right_sibling=None,label=None):
            self.attribute = attribute
            self.top = top
            self.left_child = left_child
            self.right_sibling = right_sibling 
            self.label = label


def id3(data,tree,current_node):
    
    
    #########################
    target_attribute_values = count_attribute_values(data, len(my_data[0])-1)
    if len(target_attribute_values.keys())==1:
        current_node.label = list(target_attribute_values)[0]
        return tree 
    if len(data[0])==1:   #TODO: expand some more
        current_node.label = max(target_attribute_values,key = target_attribute_values.get)
        return tree
    #########################
    
    current_node.attribute = get_information_gain(data) # attribute here is the number of the column, NOT a string 
    best_attribute_values = count_attribute_values(data, tree.root.attribute)
    previous_node = None
    for attr_value in best_attribute_values.keys():
        new_node,current_node,previous_node = tree.add_node(current_node,previous_node) #current_node as parent,previous_node as left_sibling_node 
        previous_node =new_node
        #Let Examples be the subset of Examples that have value v for A
        divided_data = divide_data(data,current_node.attribute,attr_value)
        if(len(divided_data)==0):
           pass #new_node.label= 
        else:
            id3(divided_data,tree,new_node)
            
    return current_node
'''
uses the value of a column as filter to divide the data
'''

def divide_data(data,filter_column,filter_value):
    filtered_data = [line for line in data if line[filter_column] == filter_value]
    return filtered_data


  

'''
we assume that we always calculate the entropy of the last attribute 
which is the target function value
target_attribute_values is a dictionary ex.{'No':3, 'Yes':5}. We find the entropy of a set of 3 No and 5 Yes

'''


def entropy(target_attribute_values):
    entropy=0.0
    values = target_attribute_values.values()
    sum_of_values = sum(values)
    for value in values:
        entropy-=(value/sum_of_values)*math.log2(value/sum_of_values)
    return entropy
    
'''
Separates the values of the attribute of a specific column
returns a dictionary.
this is the function that builds the dictionary that will pass as a parameter to the entropy method 
we use filter column only if we want to filter 
'''
def count_attribute_values(my_data,column,filter_column=None,attribute_value=None):
    values={}
    for line in my_data:
        if filter_column==None:
            if line[column] not in values.keys():
                values[line[column]] = 1
            else:
                values[line[column]]+=1    
        else:
            if line[filter_column]==attribute_value:
                if line[column] not in values.keys():
                    values[line[column]]=1
                else:
                    values[line[column]]+=1
               
    return values




'''
return an array of information gain for all attributes, out of which we can take everything we want, here the max
UPDATE: returns the number of the attribute in the data array
'''

def get_information_gain(my_data):
    #dictionary to store information gains
    information_gain={}
    
    #total entropy
    target_attribute_values = count_attribute_values(my_data, len(my_data[0])-1) #always interested for the last column where the target function value is
    total_entropy = entropy(target_attribute_values)
    
    ##########################
    value_given_other_attribute = {}
    for i in range(0,len(my_data[0])-1): #iterate through all the attributes, except the target attribute
        attribute_values = count_attribute_values(my_data,i)
        tempEntropy = 0.0
        for attribute in attribute_values.keys():
            value_given_other_attribute= count_attribute_values(my_data,len(my_data[0])-1,i,attribute) #here we count the target attribute GIVEN another attribute
            tempEntropy +=attribute_values[attribute]/(sum(attribute_values.values()))*entropy(value_given_other_attribute)
            print("tralala")
            
        information_gain[i] = (total_entropy - tempEntropy)
        
    
    return max(information_gain, key =information_gain.get)
    
   
   



tree = Tree()
#tree.root is the first node to examine
id3(my_data2,tree, tree.root)
#calculate the entropy of the whole data
#entropy(my_data2)

#lalal = get_information_gain(my_data2)

#tralala = count_attribute_values(my_data,4)
print("oe")
