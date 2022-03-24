import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BinarySearchTree_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()
    
    def test_on_empty(self):
        self.assertEqual([], self.__tree.to_list())
    
    ## Insertion Tests
    #Single Rotation: Right
    def test_singleRot_right_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 10, 15, 25 ]", self.__tree.in_order())
    
    def test_singleRot_right_list(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual([10, 15, 25], self.__tree.to_list())    
    
    def test_singleRot_right_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 15, 10, 25 ]", self.__tree.pre_order())   
    
    def test_singleRot_right_POST(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 10, 25, 15 ]", self.__tree.post_order())
    
    def test_singleRot_right_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual(2, self.__tree.get_height())
    
    #Single Rotation: Left
    def test_singleRot_left_IO(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 10, 15, 25 ]", self.__tree.in_order())
    
    def test_singleRot_left_list(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual([10, 15, 25], self.__tree.to_list())    
    
    def test_singleRot_left_PRO(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 15, 10, 25 ]", self.__tree.pre_order())   
    
    def test_singleRot_left_POST(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 10, 25, 15 ]", self.__tree.post_order())  
    
    def test_singleRot_left_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.assertEqual(2, self.__tree.get_height())
    
    #Single Rotation: Float
    def test_singleFlotRot_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(40)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.assertEqual("[ 5, 7, 10, 15, 20, 40 ]", self.__tree.in_order())
    
    def test_singleFlotRot_list(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(40)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.assertEqual([5, 7, 10, 15, 20, 40], self.__tree.to_list())    
    
    def test_singleFlotRot_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(40)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.assertEqual("[ 10, 5, 7, 20, 15, 40 ]", self.__tree.pre_order())
    
    def test_singleFlotRot_POST(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(40)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)  
        self.assertEqual("[ 7, 5, 15, 40, 20, 10 ]", self.__tree.post_order())
    
    def test_singleFlotRot_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(40)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)  
        self.assertEqual(3, self.__tree.get_height())
    
    
    #Test Right Left imbalance with high Volume Insertion with double and single rotations
    def test_high_volume_insertion_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.assertEqual("[ 15, 20, 25, 30, 35, 40, 45 ]", self.__tree.in_order())
    
    def test_high_volume_insertion_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.assertEqual("[ 30, 20, 15, 25, 40, 35, 45 ]", self.__tree.pre_order())  
    
    
    def test_high_volume_insertion_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45) 
        self.assertEqual("[ 15, 25, 20, 35, 45, 40, 30 ]", self.__tree.post_order())
    
    def test_high_volume_insertion_list(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.assertEqual([15, 20, 25, 30, 35, 40, 45], self.__tree.to_list())  
    
    def test_high_volume_insertion_height(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.assertEqual(3, self.__tree.get_height()) 
    
    ##Removal Tests
    #Empty check 
    def test_create_empty_tree_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(10)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.in_order())
    
    def test_create_empty_tree_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(10)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.pre_order())    
    
    def test_create_empty_tree_post(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(10)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.post_order())  
    
    def test_create_empty_tree_list(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(10)
        self.__tree.remove_element(25)
        self.assertEqual([], self.__tree.to_list()) 
    
    def test_create_empty_tree_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(15)
        self.__tree.remove_element(10)
        self.__tree.remove_element(25)
        self.assertEqual(0, self.__tree.get_height())   
    
    #Remove childless leaf
    def test_remove_childless_leaf_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)   
        self.__tree.remove_element(15)
        self.assertEqual("[ 20, 25, 30, 35, 40, 45 ]", self.__tree.in_order())
        
    def test_remove_childless_leaf_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(15)
        self.assertEqual("[ 30, 20, 25, 40, 35, 45 ]", self.__tree.pre_order())  
    
    
    def test_remove_childless_leaf_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(15)
        self.assertEqual("[ 25, 20, 35, 45, 40, 30 ]", self.__tree.post_order())    
    
    #Remove root node from tree (root is equivalent to node with children who have children)
    def test_remove_root_node_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(30)
        self.assertEqual("[ 15, 20, 25, 35, 40, 45 ]", self.__tree.in_order())
    
    def test_remove_root_node_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(30)
        self.assertEqual("[ 35, 20, 15, 25, 40, 45 ]", self.__tree.pre_order())  
    
    
    def test_remove_root_node_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45) 
        self.__tree.remove_element(30)
        self.assertEqual("[ 15, 25, 20, 45, 40, 35 ]", self.__tree.post_order())
    
    def test_remove_root_node_list(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(30)
        self.assertEqual([15, 20, 25, 35, 40, 45], self.__tree.to_list())  
    
    def test_remove_root_node_height(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(25)
        self.__tree.insert_element(45)
        self.__tree.remove_element(30)
        self.assertEqual(3, self.__tree.get_height())   
    
    #Cummulative test: complex insertion and removal. With the tests below our test cases now cover the entire scope of the 4 rotations in various situations
    def test_final_IO(self):
        self.__tree.insert_element(-1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(22)
        self.__tree.insert_element(23)
        self.__tree.insert_element(21)
        self.__tree.insert_element(18)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10) 
        self.__tree.remove_element(5)
        self.__tree.remove_element(18)
        self.assertEqual("[ -1, 2, 3, 4, 9, 10, 21, 22, 23 ]", self.__tree.in_order())
    
    def test_final_list(self):
        self.__tree.insert_element(-1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(22)
        self.__tree.insert_element(23)
        self.__tree.insert_element(21)
        self.__tree.insert_element(18)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10) 
        self.__tree.remove_element(5)
        self.__tree.remove_element(18)
        self.assertEqual([-1, 2, 3, 4, 9, 10, 21, 22, 23], self.__tree.to_list())
    
    def test_final_PRO(self):
        self.__tree.insert_element(-1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(22)
        self.__tree.insert_element(23)
        self.__tree.insert_element(21)
        self.__tree.insert_element(18)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10) 
        self.__tree.remove_element(5)
        self.__tree.remove_element(18)
        self.assertEqual("[ 9, 3, 2, -1, 4, 21, 10, 22, 23 ]", self.__tree.pre_order()) 
    
    def test_final_POST(self):
        self.__tree.insert_element(-1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(22)
        self.__tree.insert_element(23)
        self.__tree.insert_element(21)
        self.__tree.insert_element(18)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10) 
        self.__tree.remove_element(5)
        self.__tree.remove_element(18)
        self.assertEqual("[ -1, 2, 4, 3, 10, 23, 22, 21, 9 ]", self.__tree.post_order())   
    
    def test_final_height(self):
        self.__tree.insert_element(-1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(22)
        self.__tree.insert_element(23)
        self.__tree.insert_element(21)
        self.__tree.insert_element(18)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(9)
        self.__tree.insert_element(10) 
        self.__tree.remove_element(5)
        self.__tree.remove_element(18)
        self.assertEqual(4, self.__tree.get_height())       
    
    
        
        
        
if __name__ == "__main__":
    unittest.main()