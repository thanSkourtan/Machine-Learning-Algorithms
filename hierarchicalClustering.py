'''

@author: than_skourtan
'''

import math
from sys import float_info
from copy import copy
from PIL import Image,ImageDraw

class Point:
    '''
    The x-axis is indicated by the suffix 1, the y-axis is indicated by the suffix 2 etc.
    The coordinates are stored as instance variables and are also stored in a list in order
    to be better manipulated.
    '''
    def __init__(self,x1,x2,*args):
        self.x1 = x1
        self.x2 = x2
        self.list_of_coordinates= [self.x1,self.x2]
        for dimension in args:
            self.dimension = dimension
            self.list_of_coordinates.append(self.dimension)
        



class Cluster():
    '''
    distance is the value of the vertical axis. at the beginning this value is 0 for all clusters.
    x1 and *args refer to the attributes to be used to clusterize the sample data. Left and right 
    are the children nodes of the dendrogram. Does it need parent node???? for *attributes please
    see https://www.python.org/dev/peps/pep-3102/
    '''
    def __init__(self,*attributes,left=None,right=None,distance=0.0,idn=None,label=None,left_top_corner_x_coordinate=None):
        self.list_of_attributes= []
        for attribute in attributes:
            self.list_of_attributes.append(attribute)
        
        self.left = left
        self.right = right
        self.distance = distance
        self.idn = idn
        self.label = label
        self.left_top_corner_x_coordinate = left_top_corner_x_coordinate

'''
non- euclidean distance calculator, used for categorical data. All data concern presence - absence
so their values is either 0 or 1.
'''

def jaccard_index(cluster1,cluster2):
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space")
        return
    
    nominator = 0.0
    denominator = 0.0
    for i in range(0,len(cluster1.list_of_attributes)):
        if cluster1.list_of_attributes[i]==1 and cluster2.list_of_attributes[i]==1:
            nominator += 1
            denominator += 1
        elif cluster1.list_of_attributes[i] != cluster2.list_of_attributes[i]:
            denominator += 1
    return 1 - nominator/denominator

'''
counts the euclidean distance of two points in the n-dimensional space in which they are definedxs
'''
    
def euclidean_distance(cluster1, cluster2):
    if len(cluster1.list_of_attributes) != len(cluster2.list_of_attributes):
        print("The two points must be defined in the same dimensional space")
        return
    sum_of_squares = 0.0
    for i in range(0,len(cluster1.list_of_attributes)):
        sum_of_squares += pow(cluster1.list_of_attributes[i]-cluster2.list_of_attributes[i],2)
    return math.sqrt(sum_of_squares)


def agglomerative_clustering(data,distance = euclidean_distance,linkage=max):
    distances = {}
    
    cluster_list = [Cluster(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9], idn = i,label = row[10]) for i,row in enumerate(data)] # row[5], row[6], row[7] are the 3 attributes, if i want to pass other parameters i use keyword arguments instead of positional
    
    instances_num = len(cluster_list)
    
    last_idn = cluster_list[-1].idn  #gets the last id number
    
    #build the distances array
    for i in range(0,len(cluster_list)-1):
            for j in range(i+1,len(cluster_list)):
                distances[cluster_list[i].idn,cluster_list[j].idn]=distance(cluster_list[i],cluster_list[j])
    
    while(len(cluster_list)!=1):
        shortest = float_info.max
        shortest_cluster = ()
        
        changed = False
        #find the shortest distance
        for i in range(0,len(cluster_list)-1):
            if cluster_list[i].idn!=-1:
                for j in range(i+1,len(cluster_list)):
                    if cluster_list[j].idn!=-1:
                        if distances[cluster_list[i].idn,cluster_list[j].idn] < shortest: #shortest is used only here
                            shortest = distances[cluster_list[i].idn,cluster_list[j].idn] 
                            shortest_cluster = (copy(cluster_list[i]),copy(cluster_list[j]))
                            shortest_cluster_temp = cluster_list[i],cluster_list[j]
                            position_in_cluster_list = (i,j)
                            changed = True
        
        if not changed: 
            break
        '''
        TODO: TO REMOVE SHORTEST_CLUSTER_TEMP AND SEE WHAT THING COPY IN SHORTEST_CLUSTER AFFECTS
        '''
        #create a new cluster
        
        temporary_cluster = Cluster(left = shortest_cluster_temp[0], right = shortest_cluster_temp[1],distance = shortest,idn= last_idn+1)            
        last_idn +=1
                
                
        cluster_list[position_in_cluster_list[0]].idn=-1
        cluster_list[position_in_cluster_list[1]].idn=-1
        
        
        #we now restructure the distances dictionary
        
        temp_dictionary = {}
        
        for cluster in cluster_list:
            if cluster.idn!=-1:
                low_first = min(cluster.idn,shortest_cluster[0].idn)
                high_first = max(cluster.idn,shortest_cluster[0].idn)
                
                low_second  = min(cluster.idn,shortest_cluster[1].idn)
                high_second = max(cluster.idn,shortest_cluster[1].idn)
                
                temp_dictionary[cluster.idn,temporary_cluster.idn]=max(distances[low_first,high_first], distances[low_second,high_second])
                del distances[low_first,high_first]
                del distances[low_second,high_second]
        
        del distances[shortest_cluster[0].idn,shortest_cluster[1].idn]
        
        #insert the new cluster to the list
        cluster_list.append(temporary_cluster)
        
        #merge the two dictionaries
        distances.update(temp_dictionary)
        
        print("oe")
    return cluster_list,instances_num

'''
finds the mean of a list 
'''

def mean(data_list):
    return sum(data_list)/float(len(data_list))

'''
finds the standard deviation of a list
'''

def standard_deviation(data_list):
    mean_of_list = round(mean(data_list),3)
    sum_of_squares = 0.0
    for value in data_list:
        sum_of_squares += round(pow(value - mean_of_list,2),3)
    return math.sqrt(sum_of_squares/(len(data_list)-1))


'''
standardizes the values of the list passed as argument
'''

def standardisation(data_list):
    m = mean(data_list)
    sd = standard_deviation(data_list)
    return [((row-m)/sd) for row in data_list]

    
'''
returns an attribute(variable) list out of a two dimensional data list
'''

def pick_up_column(data,column_no):
    attribute_list = []
    for row in data:
        attribute_list.append(row[column_no])
    return attribute_list

    


data2 = [[1,1,1,0,1,0,0,1,1,1,"A"],
         [1,1,0,1,1,0,0,0,0,1,"B"],
         [0,1,1,0,1,0,0,1,0,0,"C"],
         [0,0,0,1,0,1,0,0,0,0,"D"],
         [1,1,1,0,1,0,1,1,1,0,"E"],
         [0,1,0,1,1,0,0,0,0,1,"F"],
         [0,1,1,0,1,1,0,1,1,0,"G"]]


'''sample data'''
data = [[0,2,9,14,2,72,4.8,3.5,"S"],
        [26,4,13,11,0,75,2.8,2.5,"C"],
        [0,10,9,8,0,59,5.4,2.7,"C"],
        [0,0,15,3,0,64,8.2,2.9,"S"],
        [13,5,3,10,7,61,3.9,3.1,"C"],
        [31,21,13,16,5,94,2.6,3.5,"G"],
        [9,6,0,11,2,53,4.6,2.9,"S"],
        [2,0,0,0,1,61,5.1,3.3,"C"],
        [17,7,10,14,6,68,3.9,3.4,"C"],
        [0,5,26,9,0,69,10.0,3.0,"S"],
        [0,8,8,6,7,57,6.5,3.3,"C"],
        [14,11,13,15,0,84,3.8,3.1,"S"],
        [0,0,19,0,6,53,9.4,3.0,"S"],
        [13,0,0,9,0,83,4.7,2.5,"C"],
        [4,0,10,12,0,100,6.7,2.8,"C"],
        [42,20,0,3,6,84,2.8,3.0,"G"],
        [4,0,0,0,0,96,6.4,3.1,"C"],
        [21,15,33,20,0,74,4.4,2.8,"G"],
        [2,5,12,16,3,79,3.1,3.6,"S"],
        [0,10,14,9,0,73,5.6,3.0,"S"],
        [8,0,0,4,6,59,4.3,3.4,"C"],
        [35,10,0,9,17,54,1.9,2.8,"S"],
        [6,7,1,17,10,95,2.4,2.9,"G"],
        [18,12,20,7,0,64,4.3,3.0,"C"],
        [32,26,0,23,0,97,2.0,3.0,"G"],
        [32,21,0,10,2,78,2.5,3.4,"S"],
        [24,17,0,25,6,85,2.1,3.0,"G"],
        [16,3,12,20,2,92,3.4,3.3,"G"],
        [11,0,7,8,0,51,6.0,3.0,"S"],
        [24,37,5,18,1,99,1.9,2.9,"G"]]




def print_cluster(cluster,first_available,draw):
    
    horizontal_margins = 100
    cluster_width = 40
    width = cluster_width * (instances_num+1)
    height = 600
    vertical_margins = 100
    cluster_height = lambda cluster_distance :  ((height - vertical_margins) * cluster_distance)/cluster_list[-1].distance
    y_axis_split=5
    
    #base case, first print the labels, then the first clusters
    if cluster.left is None and cluster.right is None:
        draw.text((horizontal_margins/2 + cluster_width * first_available,height - vertical_margins/2+6),cluster.label,fill=(255,0,0)) #fill = xroma
        cluster.left_top_corner_x_coordinate = horizontal_margins/2 + cluster_width * first_available
        first_available +=1
        return cluster,first_available   
    else: 
        child_one,first_available = print_cluster(cluster.left,first_available,draw)
        child_two,first_available = print_cluster(cluster.right,first_available,draw)
        
        x1= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else cluster_width/2)
        y1= -cluster_height(cluster.left.distance) - vertical_margins/2 + height
        x2= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else cluster_width/2)
        y2= -cluster_height(cluster.distance) - vertical_margins/2+height
        
        x3= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else cluster_width/2)
        y3= -cluster_height(cluster.right.distance)- vertical_margins/2 + height
        x4= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else cluster_width/2)
        y4= -cluster_height(cluster.distance) - vertical_margins/2 + height
        
        
        
        #vertical line                                            
        draw.line((x1,y1,x2,y2),fill=(255,0,0))
        
        #horizontal line
        draw.line((x2,y2,x4,y4),fill=(255,0,0))
        
        #vertical line                                            
        draw.line((x3,y3,x4,y4),fill=(255,0,0))
            
        cluster.left_top_corner_x_coordinate = x2
        
        return cluster,first_available
        
    print("oe")
  

def print_dendrogram2(cluster_list,instances_num):
    horizontal_margins = 100
    cluster_width = 40
    width = cluster_width * (instances_num+1)
    
    height = 600
    vertical_margins = 100
    
    cluster_height = lambda cluster_distance :  ((height - vertical_margins) * cluster_distance)/cluster_list[-1].distance
    
    y_axis_split=5
    
    
    # Create a new image with a white background
    image=Image.new('RGB',(width + horizontal_margins,height),(255,255,255))
    draw=ImageDraw.Draw(image)
    
    #x-axis
    draw.line((horizontal_margins/2,height-vertical_margins/2,width+horizontal_margins/2,height-vertical_margins/2),fill=(255,0,0))
    
    #y-axis
    draw.line((horizontal_margins/2,height-vertical_margins/2,horizontal_margins/2,vertical_margins/2),fill=(255,0,0))
    counter = 0
    #print some random heights
    for i in range(y_axis_split+1):
        draw.text((horizontal_margins/2-30,vertical_margins/2+(height-vertical_margins)/y_axis_split*counter),str(round(cluster_list[-1].distance*(1-counter*1/y_axis_split),2)),fill=(255,0,0))
        counter +=1
    
    #print the heights of all clusters
    for cluster in cluster_list:
        draw.text((horizontal_margins/2-30,-cluster_height(cluster.distance) - vertical_margins/2+height),str(round(cluster.distance,2)),fill=(255,0,0))
    
    print_cluster(cluster_list[-1],1,draw)
    
    image.show()
    
    #############################################################################################










def print_dendrogram(cluster_list,instances_num):
    
    horizontal_margins = 100
    cluster_width = 40
    width = cluster_width * (instances_num+1)
    
    height = 600
    vertical_margins = 100
    
    cluster_height = lambda cluster_distance :  ((height - vertical_margins) * cluster_distance)/cluster_list[-1].distance
    
    y_axis_split=5
    
    
    # Create a new image with a white background
    image=Image.new('RGB',(width + horizontal_margins,height),(255,255,255))
    draw=ImageDraw.Draw(image)
    
    #x-axis
    draw.line((horizontal_margins/2,height-vertical_margins/2,width+horizontal_margins/2,height-vertical_margins/2),fill=(255,0,0))
    
    #y-axis
    draw.line((horizontal_margins/2,height-vertical_margins/2,horizontal_margins/2,vertical_margins/2),fill=(255,0,0))
    counter = 0
    #print some random heights
    for i in range(y_axis_split+1):
        draw.text((horizontal_margins/2-30,vertical_margins/2+(height-vertical_margins)/y_axis_split*counter),str(round(cluster_list[-1].distance*(1-counter*1/y_axis_split),2)),fill=(255,0,0))
        counter +=1
    
    #print the heights of all clusters
    for cluster in cluster_list:
        draw.text((horizontal_margins/2-30,-cluster_height(cluster.distance) - vertical_margins/2+height),str(round(cluster.distance,2)),fill=(255,0,0))
    
    
    
    counter = 1
    for i in range(instances_num,len(cluster_list)):
        # if the left or right foot of the cluster is onto the x-axis, print the label of the data instance 
        if cluster_list[i].left.left is None:
            draw.text((horizontal_margins/2 + cluster_width * counter,height - vertical_margins/2+6),cluster_list[i].left.label,fill=(255,0,0)) #fill = xroma
            cluster_list[i].left.left_top_corner_x_coordinate=horizontal_margins/2 + cluster_width * counter
            counter +=1
        if cluster_list[i].right.right is None:
            draw.text((horizontal_margins/2 + cluster_width * counter,height - vertical_margins/2+6),cluster_list[i].right.label,fill=(255,0,0)) #fill = xroma
            cluster_list[i].right.left_top_corner_x_coordinate=horizontal_margins/2 + cluster_width * counter
            counter+=1
            
        #vertical line                                            
        draw.line((cluster_list[i].left.left_top_corner_x_coordinate + (0.0 if cluster_list[i].left.left is None else cluster_width/2),
                    -cluster_height(cluster_list[i].left.distance) - vertical_margins/2 + height,
                    cluster_list[i].left.left_top_corner_x_coordinate + (0.0 if cluster_list[i].left.left is None else cluster_width/2),
                    -cluster_height(cluster_list[i].distance) - vertical_margins/2+height),
                    fill=(255,0,0))
        
        #horizontal line
        draw.line((cluster_list[i].left.left_top_corner_x_coordinate + (0.0 if cluster_list[i].left.left is None else cluster_width/2),
                  -cluster_height(cluster_list[i].distance) - vertical_margins/2+height,
                  cluster_list[i].right.left_top_corner_x_coordinate + (0 if cluster_list[i].right.right is None else cluster_width/2),
                  -cluster_height(cluster_list[i].distance) - vertical_margins/2 + height),
                  fill=(255,0,0))
        
        #vertical line
        draw.line((cluster_list[i].right.left_top_corner_x_coordinate + (0 if cluster_list[i].right.right is None else cluster_width/2),
                    -cluster_height(cluster_list[i].right.distance)- vertical_margins/2 + height,
                    cluster_list[i].right.left_top_corner_x_coordinate + (0 if cluster_list[i].right.right is None else cluster_width/2),
                    -cluster_height(cluster_list[i].distance) - vertical_margins/2 + height),
                    fill=(255,0,0))
        
        cluster_list[i].left_top_corner_x_coordinate = cluster_list[i].left.left_top_corner_x_coordinate + (0.0 if cluster_list[i].left.left is None else cluster_width/2)
        #break
        print("lala")
    
    
    image.show()
    



cluster_list, instances_num = agglomerative_clustering(data2)

#print_dendrogram(cluster_list,instances_num)

print_dendrogram2(cluster_list,instances_num)



