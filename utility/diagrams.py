"""Includes functions 

This module uses the Image and ImageDraw modules of the Python Imaging Library(PIL) in order to create a new Image and then draw the lines
that will eventually consist of the diagram, dendrogram etc. Currently, it consists of the functions:
print_dendrogram
__print_cluster

@author: than_skourtan
"""
from PIL import Image, ImageDraw



class Diagram:
    
    def __init__(self,horizontal_margins=100, height=700, vertical_margins=100, width = 1000, cluster_width = 40):
        """The constructor provides some optional values for the diagram's attributes. Values are in pixels.
        
        horizontal_margins = the total length of margins. for example when horizontal_margins =100 then left_margin = right_margin = 50
        vertical_margins = vertical margins on the other hand are part or the width. so height 700 includes the vertical_margins. TODO: fix it.
        
        """
        self.horizontal_margins = horizontal_margins
        self.height = height
        self.vertical_margins = vertical_margins
        self.width = width
        self.cluster_width = cluster_width
        
        # Create a new image with a white background
        self.image=Image.new('RGB', (self.width + self.horizontal_margins, self.height), (255, 255, 255))
        self.draw=ImageDraw.Draw(self.image)
        
        #x-axis
        self.draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.width+ self.horizontal_margins/2, 
                   self.height - self.vertical_margins/2), fill=(0, 0, 0))
        
        #y-axis
        self.draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, self.vertical_margins/2), fill=(0, 0, 0))
        
        
        
    #def scatter_plot(self, x_axis = [], y_axis =[], data_instances = None, r = 2):
    def scatter_plot(self, *args, r = 2):        
        """Plots the points indicated by the coordinates x, y, passed as parameters."""
        
        argument_types = tuple(arg.__class__ for arg in args)
        typemap = {(list, list):self.scatter_plot_axis, (list,) : self.scatter_plot_data_instances}
        
        if argument_types in typemap:
            return typemap[argument_types](*args)
        else:
            print("Input a list of data instances or two lists with the x, y values")
        
    def scatter_plot_axis(self, x_axis = [], y_axis =[],  r = 2):
        
        if len(x_axis) != len(y_axis):
            print("The x_axis length must be equal to the y_axis length")
            return
                
        largest_x = max(x_axis)
        largest_y = max(y_axis)
        
        #uses the rule of three 
        point_height = lambda y : self.vertical_margins/2 + (self.height - self.vertical_margins) * (1 - y/largest_y)  #because y-axis is reversed
        point_width = lambda x :  self.horizontal_margins/2 + (self.width * x/largest_x) # because the largest x will have width equal to width - hor_margins/2
        
        for i in range(len(x_axis)):
            self.draw.ellipse(( point_width(x_axis[i]) - r,point_height(y_axis[i]) - r,point_width(x_axis[i]) + r,point_height(y_axis[i]) + r),fill=(255,0,0))
        
        
        
        ################################################ lines for TSP
        '''x_first = -1
        y_first = -1
        for i in range(len(x_axis)):
            if i == 0: # if first 
                x_previous = x_axis[i]
                y_previous = y_axis[i]
                x_first = x_axis[i]
                y_first = y_axis[i]
            elif i == (len(x_axis) - 1):
                draw.line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_previous), point_height(y_previous)), fill=(255, 0, 0))
                draw.line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_first), point_height(y_first)), fill=(255, 0, 0))
            else:
                draw.line((point_width(x_axis[i]),point_height(y_axis[i]), point_width(x_previous), point_height(y_previous)), fill=(255, 0, 0))
                x_previous = x_axis[i]
                y_previous = y_axis[i]'''
        
        
        
        #print the y-values of all points
        '''for y in y_axis:
            draw.text((self.horizontal_margins/2 - 30, - cluster_height(cluster.distance) - self.vertical_margins/2 + self.height), 
                      str(round(cluster.distance, 2)), fill=(255, 0, 0))
        '''
        
        self.image.show()
        
    
    def scatter_plot_data_instances(self, data_instances, r = 2):
        """Plots data instances"""
        
        for data_instance in data_instances:
            if data_instance.feature_vector.size != 2:
                print("The data should have only 2 features.")
                return
        x_axis = [data_instance.feature_vector[0] for data_instance in data_instances]
        y_axis = [data_instance.feature_vector[1] for data_instance in data_instances]
        self.scatter_plot_axis(x_axis, y_axis)

    def print_dendrogram(self, cluster_list, instances_num):
        
        self.width = self.cluster_width * (instances_num + 1) #in the case of a dendrogram, width varies according the the number of clusters
        
        #uses the rule of three to find the height of a cluster in the diagram
        cluster_height = lambda cluster_distance :  ((self.height - self.vertical_margins) * cluster_distance)/cluster_list[-1].distance 
        
        y_axis_split = 5
        
        # Create a new image with a white background
        image=Image.new('RGB', (self.width + self.horizontal_margins, self.height), (255, 255, 255))
        draw=ImageDraw.Draw(image)
        
        #x-axis
        draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.width+ self.horizontal_margins/2, 
                   self.height - self.vertical_margins/2), fill=(255, 0, 0))
        
        #y-axis
        draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, self.vertical_margins/2), fill=(255, 0, 0))
        
        #print some random heights
        counter = 0
        for i in range(y_axis_split+1):
            draw.text((self.horizontal_margins/2-30, self.vertical_margins/2+(self.height - self.vertical_margins)/y_axis_split*counter), 
                      str(round(cluster_list[-1].distance*(1-counter*1/y_axis_split), 2)),fill=(255, 0, 0))
            counter +=1
        
        #print the heights of all clusters
        for cluster in cluster_list:
            draw.text((self.horizontal_margins/2 - 30, - cluster_height(cluster.distance) - self.vertical_margins/2 + self.height), 
                      str(round(cluster.distance, 2)), fill=(255, 0, 0))
        
        self.__print_cluster(cluster_list[-1], 1, draw, cluster_list[-1].distance)
        
      
        image.show()
            
    def __print_cluster(self, cluster, first_available, draw, highest_cluster_distance):
        """Prints the three lines a cluster is consisted of.
        A private method called only from the print_dendrogram function in order to print all the clusters of the dendrogram. A cluster is graphically made
        out of 3 intersecting lines creating a table - like shape. In order the algorithm implemented in this function to find the coordinates needed for 
        each line it traverses recursively the binary tree of clusters, represented by the cluster_list, moving from one cluster to the other through their 
        left and right pointers to its descendants. It starts from the upper cluster and it finds its way down to the lowest clusters of the tree.
        
        Parameters:
            cluster(Cluster): the cluster to be drawn
            first_available(int): a counter used by the lowest clusters in order to indicate which is the first available position in the horizontal axis in order  
                the current cluster to be drawn
            draw(ImageDraw): An object to draw on the Image
            highest_cluster_distance(double): the distance attribute of the highest cluster, the one with the largest distance, which is also the last one
                at the cluster_list
            number_of_clusters: 
        
        Returns: 
            the current cluster and the first_available counter
        
        """
        
        cluster_height = lambda cluster_distance :  ((self.height - self.vertical_margins) * cluster_distance)/highest_cluster_distance
        
        #base case, first print the labels, then the first clusters
        if (cluster.left is None and cluster.right is None):
            draw.text((self.horizontal_margins/2 + self.cluster_width * first_available, self.height - self.vertical_margins/2+6), 
                      str(cluster.label), fill=(0, 0, 0))
            cluster.left_top_corner_x_coordinate = self.horizontal_margins/2 + self.cluster_width * first_available
            first_available +=1
            return cluster, first_available   
        else: 
            child_one, first_available = self.__print_cluster(cluster.left, first_available, draw, highest_cluster_distance)
            child_two, first_available = self.__print_cluster(cluster.right, first_available, draw, highest_cluster_distance)
            
            x1= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else self.cluster_width/2)
            y1= -cluster_height(cluster.left.distance) - self.vertical_margins/2 + self.height
            x2= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else self.cluster_width/2)
            y2= -cluster_height(cluster.distance) - self.vertical_margins/2 + self.height
            
            x3= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else self.cluster_width/2)
            y3= -cluster_height(cluster.right.distance)- self.vertical_margins/2 + self.height
            x4= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else self.cluster_width/2)
            y4= -cluster_height(cluster.distance) - self.vertical_margins/2 + self.height
            
            #vertical line                                            
            draw.line((x1, y1, x2, y2),fill=(0, 0, 0), width=1)
            
            #horizontal line
            draw.line((x2, y2, x4, y4),fill=(0, 0, 0), width=1)
            
            #vertical line                                            
            draw.line((x3, y3, x4, y4),fill=(0, 0, 0), width=1)
                
            cluster.left_top_corner_x_coordinate = x2
            
            return cluster, first_available
            