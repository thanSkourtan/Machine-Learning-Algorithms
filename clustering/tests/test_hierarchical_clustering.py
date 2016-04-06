"""""
@author: than_skourtan
"""


import unittest
from csv import reader
from utility.diagrams import Diagram
from clustering.hierarchical_clustering import agglomerative_clustering

class TestHierarchicalClustering(unittest.TestCase):
    
    
    def setUp(self):
        data2 = [["A", 1, 1, 1, 0, 1, 0, 0, 1, 1, 1], 
                 ["B", 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],  
                 ["C", 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],  
                 ["D", 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  
                 ["E", 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],  
                 ["F", 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],  
                 ["G", 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
        
        
        
        
        '''sample data'''
        data = [["S", 0, 2, 9, 14, 2, 72, 4.8, 3.5],  
                ["C", 26, 4, 13, 11, 0, 75, 2.8, 2.5],  
                ["C", 0, 10, 9, 8, 0, 59, 5.4, 2.7],  
                ["S", 0, 0, 15, 3, 0, 64, 8.2, 2.9],  
                ["C", 13, 5, 3, 10, 7, 61, 3.9, 3.1],  
                ["G", 31, 21, 13, 16, 5, 94, 2.6, 3.5],  
                ["S", 9, 6, 0, 11, 2, 53, 4.6, 2.9],  
                ["C", 2, 0, 0, 0, 1, 61, 5.1, 3.3],  
                ["C", 17, 7, 10, 14, 6, 68, 3.9, 3.4],  
                ["S", 0, 5, 26, 9, 0, 69, 10.0, 3.0],  
                ["C", 0, 8, 8, 6, 7, 57, 6.5, 3.3],  
                ["S", 14, 11, 13, 15, 0, 84, 3.8, 3.1],  
                ["S", 0, 0, 19, 0, 6, 53, 9.4, 3.0],  
                ["C", 13, 0, 0, 9, 0, 83, 4.7, 2.5],  
                ["C", 4, 0, 10, 12, 0, 100, 6.7, 2.8],  
                ["G", 42, 20, 0, 3, 6, 84, 2.8, 3.0],  
                ["C", 4, 0, 0, 0, 0, 96, 6.4, 3.1],  
                ["G", 21, 15, 33, 20, 0, 74, 4.4, 2.8],  
                ["S", 2, 5, 12, 16, 3, 79, 3.1, 3.6],  
                ["S", 0, 10, 14, 9, 0, 73, 5.6, 3.0],  
                ["C", 8, 0, 0, 4, 6, 59, 4.3, 3.4],  
                ["S", 35, 10, 0, 9, 17, 54, 1.9, 2.8],  
                ["G", 6, 7, 1, 17, 10, 95, 2.4, 2.9],  
                ["C", 18, 12, 20, 7, 0, 64, 4.3, 3.0],  
                ["G", 32, 26, 0, 23, 0, 97, 2.0, 3.0],  
                ["S", 32, 21, 0, 10, 2, 78, 2.5, 3.4],  
                ["G", 24, 17, 0, 25, 6, 85, 2.1, 3.0],  
                ["G", 16, 3, 12, 20, 2, 92, 3.4, 3.3],  
                ["S", 11, 0, 7, 8, 0, 51, 6.0, 3.0],  
                ["G", 24, 37, 5, 18, 1, 99, 1.9, 2.9]]
        
        
        op = open("features.csv")
        
        lalalala = reader(op)
        
        self.my_other_data = []
        
        
        
        my_precious_data = [line for line in lalalala]
        
        op.close()
        
        for i in range(len(my_precious_data)):
            self.my_other_data += [row.split(";") for row in my_precious_data[i]]
            
            
            for i in range(len(self.my_other_data)):
                self.my_other_data[i] = [float(element) for element in self.my_other_data[i]]
            
            print(self.my_other_data)
        
    
    def test_hierarchical_clustering(self):
        
        
            
            
        cluster_list, instances_num = agglomerative_clustering(self.my_other_data)
        
        
        for oeoeoe in cluster_list:
            print(oeoeoe.distance, " left: ",  (oeoeoe.left.label if oeoeoe.left is not None else 0),  "right: ", (oeoeoe.right.label if oeoeoe.right is not None else 0))
            
            
        print(len(cluster_list))
        
        
        diagram = Diagram()
        
        diagram.print_dendrogram(cluster_list, instances_num)


"""
cluster_list, instances_num = agglomerative_clustering(data2)
print_dendrogram(cluster_list,instances_num)

"""
#divisive_clustering(data2)





if __name__ == "__main__":
    unittest.main()

