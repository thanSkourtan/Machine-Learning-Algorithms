"""Includes functions 

This module uses the Image and ImageDraw modules of the Python Imaging Library(PIL) in order to create a new Image and then draw the lines
that will eventually consist of the diagram, dendrogram etc. Currently, it consists of the functions:
print_dendrogram
__print_cluster

@author: than_skourtan
"""
#from PIL import Image, ImageDraw
from tkinter import *
import clustering.data_instance as din


class Diagram():
    
    def __init__(self,horizontal_margins=100, height=700, vertical_margins=100, width = 1000, cluster_width = 22):
        """The constructor provides some optional values for the diagram's attributes. Values are in pixels.
        
        horizontal_margins = the total length of margins. for example when horizontal_margins =100 then left_margin = right_margin = 50
        vertical_margins = vertical margins on the other hand are part or the width. so height 700 includes the vertical_margins. TODO: fix it.
        
        """
        
        self.horizontal_margins = horizontal_margins
        self.height = height
        self.vertical_margins = vertical_margins
        self.width = width
        self.cluster_width = cluster_width
        
        self.root = Tk()
        
        #tkinter code to make the canvas scrollable. see http://stackoverflow.com/questions/7727804/python-and-tkinter-using-scrollbars-on-a-canvas
        
        self.frame = Frame(self.root,width = self.width + self.horizontal_margins, height = self.height)
        self.frame.grid(row=0,column=0)
        
        self.canvas = Canvas(self.frame,bg='white',  width = self.width + self.horizontal_margins, height=self.height, scrollregion=(0,0,15000,0))
        
        hbar=Scrollbar(self.frame, orient = HORIZONTAL)
        hbar.pack(side = BOTTOM,fill=X)
        hbar.config(command = self.canvas.xview)
        #vbar=Scrollbar(frame,orient=VERTICAL)
        #vbar.pack(side=RIGHT,fill=Y)
        #vbar.config(command=canvas.yview)
        self.canvas.config(width= self.width + self.horizontal_margins,height = self.height, xscrollcommand=hbar.set)
        self.canvas.pack(side = LEFT, expand=True,fill=BOTH)
        
        #self.canvas = Canvas(self.root, bg = "white", height = self.height, width = self.width + self.horizontal_margins)
        #self.canvas.pack()
        self.canvas.create_line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.width+ self.horizontal_margins/2, 
                   self.height - self.vertical_margins/2), fill = "blue")
        self.canvas.create_line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, 
                                 self.vertical_margins/2), fill = "blue")
        """
        # Create a new image with a white background
        self.image=Image.new('RGB', (self.width + self.horizontal_margins, self.height), (255, 255, 255))
        self.draw=ImageDraw.Draw(self.image)
        #x-axis
        self.draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.width+ self.horizontal_margins/2, 
                   self.height - self.vertical_margins/2), fill=(0, 0, 0))
        #y-axis
        self.draw.line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, self.vertical_margins/2), fill=(0, 0, 0))
        """
        
    
    def point_relative_dimensions(self, x, y, largest_x, largest_y):
        #uses the rule of three
        x_relative = self.horizontal_margins/2 + (self.width * x/largest_x) # because the largest x will have width equal to width - hor_margins/2
        y_relative = self.vertical_margins/2 + (self.height - self.vertical_margins) * (1 - y/largest_y)  #because y-axis is reversed
        return x_relative, y_relative

    
    def __plot_the_points(self, x_axis, y_axis, r):
        largest_x = max(x_axis)
        largest_y = max(y_axis)
        
        for i in range(len(x_axis)):
            #self.draw.ellipse(( point_width(x_axis[i]) - r,point_height(y_axis[i]) - r,point_width(x_axis[i]) + r,point_height(y_axis[i]) + r),fill=(255,0,0))
            x,y = self.point_relative_dimensions(x_axis[i], y_axis[i], largest_x, largest_y) 
            self.canvas.create_oval(x - r, y - r, x + r, y + r, outline= "red", fill = "red") 
    
    def __plot_the_lines(self, x_axis, y_axis):
        largest_x = max(x_axis)
        largest_y = max(y_axis)
        
        for i in range(0, len(x_axis)):
            for j in range(i + 1, len(x_axis)):
                self.canvas.create_line((self.point_relative_dimensions(x_axis[i], y_axis[i], largest_x, largest_y), self.point_relative_dimensions(x_axis[j], y_axis[j], largest_x, largest_y)), fill = "blue")
        """
        for i in range(0, len(x_axis)-1):
            self.canvas.create_line((point_width(x_axis[i]), point_height(y_axis[i]), point_width(x_axis[i+1]), point_height(y_axis[i+1])), fill = "blue")
        """
    
    
    def scatter_plot(self, *args, r = 2):        
        """Plots the points indicated by the coordinates x, y, passed as parameters."""
        
        argument_types = tuple(arg.__class__ for arg in args)
        typemap = {(list, list):self.__scatter_plot_axis, (list,) : self.__scatter_plot_data_instances}
        
        if argument_types in typemap:
            return typemap[argument_types](*args)
        else:
            print("Input a list of data instances or two lists with the x, y values")
        
    def __scatter_plot_axis(self, x_axis = [], y_axis =[],  r = 2):
        
        if len(x_axis) != len(y_axis):
            print("The x_axis length must be equal to the y_axis length")
            return
        self.__plot_the_points(x_axis, y_axis, r)
        self.root.wm_title("scatter plot")
        self.root.mainloop()
        
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
    
    def __scatter_plot_data_instances(self, data_instances, r = 2):
        """Plots data instances"""
        
        x_axis, y_axis = din.data_instances_to_lists(data_instances)
        self.__plot_the_points(x_axis, y_axis, r)
        self.root.wm_title("scatter plot") 
        self.root.mainloop()

        
    def complete_graph_plot(self, data_instances, r = 5):
        x_axis, y_axis = din.data_instances_to_lists(data_instances)
        self.__plot_the_points(x_axis, y_axis, r)
        self.__plot_the_lines(x_axis, y_axis)
        self.root.wm_title("graph")
        self.root.mainloop()
        
        
    def root_size_change_handler(self, event):
        #size = (self.root.winfo_reqwidth(), self.root.winfo_reqheight())
        #self.canvas.config(scrollregion='0 0 %s %s' %size)
        if self.root.winfo_width() != self.canvas.winfo_width():
            self.frame.config(width = self.root.winfo_width())
            self.frame.config(height = self.root.winfo_height())
    
    def plot_mst_graph(self, mst, r = 2):
        x_axis, y_axis = din.data_instances_to_lists(mst)
        self.__plot_the_points(x_axis, y_axis, r)
        largest_x = max(x_axis)
        largest_y = max(y_axis)
        
        for node in mst:
            if node.parent is not None: 
                self.canvas.create_line(self.point_relative_dimensions(node.feature_vector[0], node.feature_vector[1], largest_x, largest_y), 
                                        self.point_relative_dimensions(node.parent.feature_vector[0], node.parent.feature_vector[1], 
                                        largest_x, largest_y), fill = "blue")
                #TODO: currently just for debugging reasons
                self.canvas.create_text(self.point_relative_dimensions(node.feature_vector[0], node.feature_vector[1]-2, largest_x, largest_y), 
                                        text = str(node.id), fill= "red")
        
        
        self.root.mainloop()
                


    def print_dendrogram(self, cluster_list, instances_num):
        
        self.width = self.cluster_width * (instances_num + 1) #in the case of a dendrogram, width varies according the the number of clusters
        
        # http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        self.root.wm_title("dendrogram")    
        self.root.bind("<Configure>", self.root_size_change_handler)
        
        #uses the rule of three to find the height of a cluster in the diagram
        cluster_height = lambda cluster_distance :  ((self.height - self.vertical_margins) * cluster_distance)/cluster_list[-1].distance 
        
        y_axis_split = 5
        
        # Create a new image with a white background
        #image=Image.new('RGB', (self.width + self.horizontal_margins, self.height), (255, 255, 255))
        #draw=ImageDraw.Draw(image)
        
        #x-axis
        self.canvas.create_line(self.horizontal_margins/2, self.height - self.vertical_margins/2, self.width+ self.horizontal_margins/2, 
                   self.height - self.vertical_margins/2, fill = "blue")
        
        #y-axis
        self.canvas.create_line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, self.vertical_margins/2), fill = "blue")
        
        #print some random heights
        counter = 0
        for i in range(y_axis_split+1):
            self.canvas.create_text((self.horizontal_margins/2-30, self.vertical_margins/2+(self.height - self.vertical_margins)/y_axis_split*counter), 
                      text = str(round(cluster_list[-1].distance*(1-counter*1/y_axis_split), 2)), fill= "red")
            counter +=1
        
        #print the heights of all clusters
        for cluster in cluster_list:
            self.canvas.create_text((self.horizontal_margins/2 - 30, - cluster_height(cluster.distance) - self.vertical_margins/2 + self.height), 
                      text = str(round(cluster.distance, 2)), fill= "red")
        
        self.__print_cluster(cluster_list[-1], 1, cluster_list[-1].distance)
        
        self.root.mainloop()
            
    def __print_cluster(self, cluster, first_available, highest_cluster_distance):
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
            self.canvas.create_text((self.horizontal_margins/2 + self.cluster_width * first_available, self.height - self.vertical_margins/2+6), 
                      text = str(int(cluster.label)), fill= "black")
            cluster.left_top_corner_x_coordinate = self.horizontal_margins/2 + self.cluster_width * first_available
            first_available +=1
            return cluster, first_available   
        else: 
            child_one, first_available = self.__print_cluster(cluster.left, first_available, highest_cluster_distance)
            child_two, first_available = self.__print_cluster(cluster.right, first_available,  highest_cluster_distance)
            
            x1= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else self.cluster_width/2)
            y1= -cluster_height(cluster.left.distance) - self.vertical_margins/2 + self.height
            x2= child_one.left_top_corner_x_coordinate + (0.0 if child_one.left is None else self.cluster_width/2)
            y2= -cluster_height(cluster.distance) - self.vertical_margins/2 + self.height
            
            x3= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else self.cluster_width/2)
            y3= -cluster_height(cluster.right.distance)- self.vertical_margins/2 + self.height
            x4= child_two.left_top_corner_x_coordinate + (0.0 if child_two.left is None else self.cluster_width/2)
            y4= -cluster_height(cluster.distance) - self.vertical_margins/2 + self.height
            
            
            
            #self.canvas.create_line((self.horizontal_margins/2, self.height - self.vertical_margins/2, self.horizontal_margins/2, self.vertical_margins/2), fill = "blue")        
            
            #vertical line                                            
            self.canvas.create_line((x1, y1, x2, y2),fill = "black", width=1)
            
            #horizontal line
            self.canvas.create_line((x2, y2, x4, y4),fill = "black", width=1)
            
            #vertical line                                            
            self.canvas.create_line((x3, y3, x4, y4),fill = "black", width=1)
                
            cluster.left_top_corner_x_coordinate = x2
            
            return cluster, first_available
            
            
            