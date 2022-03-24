import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BinarySearchTree_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()
    
    ##Tests on empty 
    def test_empty_tree_string_IO(self):
        self.assertEqual("[ ]", self.__tree.in_order())
    
    def test_empty_tree_string_PRO(self):
        self.assertEqual("[ ]", self.__tree.pre_order())
    
    def test_empty_tree_string_PSTO(self):
        self.assertEqual("[ ]", self.__tree.post_order())
    
    def test_empty_tree(self):
        self.assertEqual(0, self.__tree.get_height())
    
    ##Insertion Tests
    #Height 1
    def test_insert_on_empty_IO(self):
        self.__tree.insert_element(25)
        self.assertEqual("[ 25 ]", self.__tree.in_order())
    
    def test_insert_on_empty_PRO(self):
        self.__tree.insert_element(25)
        self.assertEqual("[ 25 ]", self.__tree.pre_order())
    
    def test_insert_on_empty_POST(self):
        self.__tree.insert_element(25)
        self.assertEqual("[ 25 ]", self.__tree.post_order())    
    
    def test_insert_on_empty_height(self):
        self.__tree.insert_element(25)
        self.assertEqual(1, self.__tree.get_height())    
    
    #Height 2
    def test_insert_on_h1_lessthan_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.assertEqual("[ 15, 25 ]", self.__tree.in_order())   
    
    def test_insert_on_h1_lessthan_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.assertEqual("[ 25, 15 ]", self.__tree.pre_order())
    
    def test_insert_on_h1_lessthan_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.assertEqual("[ 15, 25 ]", self.__tree.post_order()) 
    
    def test_insert_on_h1_lessthan_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.assertEqual(2, self.__tree.get_height())
    
    def test_insert_on_h1_gthan_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 25, 35 ]", self.__tree.in_order())   
    
    def test_insert_on_h1_gthan_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 25, 35 ]", self.__tree.pre_order())
    
    def test_insert_on_h1_gthan_PSTO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 35, 25 ]", self.__tree.post_order()) 
    
    def test_insert_on_h1_gthan_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual(2, self.__tree.get_height())    
    
    #perfect tree tests
    def test_insert_h2_perfect_tree_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 15, 20, 25 ]", self.__tree.in_order())
    
    def test_insert_h2_perfect_tree_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 20, 15, 25 ]", self.__tree.pre_order()) 
    
    def test_insert_h2_perfect_tree_PSTO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.assertEqual("[ 15, 25, 20 ]", self.__tree.post_order())         
        
    #Height 3 less than
    def test_insert_on_h2_lessthan_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 10, 15, 25 ]", self.__tree.in_order())   
    
    def test_insert_on_h2_lessthan_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 25, 15, 10 ]", self.__tree.pre_order()) 
    
    def test_insert_on_h2_lessthan_IO(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual("[ 10, 15, 25 ]", self.__tree.post_order()) 
    
    def test_insert_on_h2_lessthan_height(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.assertEqual(3, self.__tree.get_height()) 
        
    #Height 3 greather than
    def test_insert_on_h2_gthan_IO(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 10, 25, 35 ]", self.__tree.in_order())   
    
    def test_insert_on_h2_gthan_PRO(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 10, 25, 35 ]", self.__tree.pre_order())
    
    def test_insert_on_h2_gthan_PSTO(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual("[ 35, 25, 10 ]", self.__tree.post_order())
    
    def test_insert_on_h2_gthan_height(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(15)
        self.assertEqual(3, self.__tree.get_height())     
    
    #Insert height 3 with elbow
    def test_insert_h3_elbow_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.assertEqual("[ 15, 20, 25 ]", self.__tree.in_order())
    
    def test_insert_h3_elbow_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.assertEqual("[ 15, 25, 20 ]", self.__tree.pre_order())   
    
    def test_insert_h3_elbow_PSTO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.assertEqual("[ 20, 25, 15 ]", self.__tree.post_order())
    
    def test_insert_h3_elbow_height(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.assertEqual(3, self.__tree.get_height())
    
    ###Large tree insertion test
    def test_insert_h3_perfect_IO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.assertEqual("[ 15, 20, 25, 30, 35, 40, 45 ]", self.__tree.in_order())
    
    def test_insert_h3_perfect_PRO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.assertEqual("[ 30, 20, 15, 25, 40, 35, 45 ]", self.__tree.pre_order()) 
    
    def test_insert_h3_perfect_POST(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.assertEqual("[ 15, 25, 20, 35, 45, 40, 30 ]", self.__tree.post_order())    
    
    ##Removal Tests
    #empty
    def test_remove_empty_IO(self):
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.in_order())
    
    def test_remove_empty_PRO(self):
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.pre_order())   
    
    def test_remove_empty_PSTO(self):
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.post_order())    
    #Height 1
    def test_remove_h1_IO(self):
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.in_order())
    def test_remove_h1_PRO(self):
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.pre_order())   
        
    def test_remove_h1_POST(self):
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual("[ ]", self.__tree.post_order())  
    
    def test_remove_h1_height(self):
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual(0, self.__tree.get_height()) 
    
    #Height 2 Removals, tests check removal on both leaf and root
    def test_remove_h2_leaf_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual("[ 15 ]", self.__tree.in_order())
    
    def test_remove_h2_leaf_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual("[ 15 ]", self.__tree.pre_order())
        
    def test_remove_h2_leaf_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual("[ 15 ]", self.__tree.post_order())    
    
    def test_remove_h2_leaf_height(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual(1, self.__tree.get_height()) 
    
    def test_remove_h2_root_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.in_order())
    
    def test_remove_h2_root_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.pre_order())
        
    def test_remove_h2_root_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.post_order())    
    
    def test_remove_h2_root_height(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual(1, self.__tree.get_height())   
    
    #3 nodes removal tests
    ###Remove both leaves test
    def test_remove_both_leaves_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)  
        self.__tree.remove_element(15)
        self.__tree.remove_element(25)
        self.assertEqual("[ 20 ]", self.__tree.in_order())
    
    def test_remove_both_leaves_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)  
        self.__tree.remove_element(15)
        self.__tree.remove_element(25)
        self.assertEqual("[ 20 ]", self.__tree.pre_order())  
    
    def test_remove_both_leaves_POST(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)  
        self.__tree.remove_element(15)
        self.__tree.remove_element(25)
        self.assertEqual("[ 20 ]", self.__tree.post_order()) 
    
    def test_remove_both_leaves_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)  
        self.__tree.remove_element(15)
        self.__tree.remove_element(25)
        self.assertEqual(1, self.__tree.get_height())

    def test_remove_both_leaves_IO_reverse(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.in_order())
    
    def test_remove_both_leaves_PRO_reverse(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.pre_order())   
    
    def test_remove_both_leaves_POST_reverse(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.__tree.remove_element(15)
        self.assertEqual("[ 20 ]", self.__tree.post_order()) 
    
    def test_remove_both_leaves_height_reverse(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.__tree.remove_element(15)
        self.assertEqual(1, self.__tree.get_height())
    
    ###Remove right leaf 
    def test_remove_right_leaf_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(25)
        self.assertEqual("[ 15, 20 ]", self.__tree.in_order())
    
    def test_remove_right_leaf_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(25)
        self.assertEqual("[ 20, 15 ]", self.__tree.pre_order())
    
    def test_remove_right_leaf_POST(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(25)
        self.assertEqual("[ 15, 20 ]", self.__tree.post_order())    
    
    ###Removal of left leaf
    def test_remove_left_leaf_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(15)
        self.assertEqual("[ 20, 25 ]", self.__tree.in_order()) 
    
    def test_remove_left_leaf_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(15)
        self.assertEqual("[ 20, 25 ]", self.__tree.pre_order())
    
    def test_remove_left_leaf_POST(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(15)
        self.assertEqual("[ 25, 20 ]", self.__tree.post_order())  
    
    def test_remove_left_leaf_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(15)
        self.assertEqual(2, self.__tree.get_height())    
        
    ###3 nodes 2 height, perfect, removal of root
    def test_remove_root_perfect_IO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(20)
        self.assertEqual("[ 15, 25 ]", self.__tree.in_order())
    
    def test_remove_root_perfect_PRO(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(20)
        self.assertEqual("[ 25, 15 ]", self.__tree.pre_order())
    
    def test_remove_root_perfect_POST(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(20)
        self.assertEqual("[ 15, 25 ]", self.__tree.post_order())
    
    def test_remove_root_perfect_height(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25) 
        self.__tree.remove_element(20)
        self.assertEqual(2, self.__tree.get_height())  
    
    ###Removal of joint of elbow 
    def test_remove_joint_elbowtree_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.remove_element(25)
        self.assertEqual("[ 15, 20 ]", self.__tree.in_order())
    
    def test_remove_joint_elbowtree_PRO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.remove_element(25)
        self.assertEqual("[ 15, 20 ]", self.__tree.pre_order())
    
    def test_remove_joint_elbowtree_POST(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.remove_element(25)
        self.assertEqual("[ 20, 15 ]", self.__tree.post_order())
    
    def test_remove_joint_elbowtree_IO(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(20)
        self.__tree.remove_element(25)
        self.assertEqual(2, self.__tree.get_height())    
    
    ###Removal tests on perfect tree of height 3 (testing removal of node at h2 which has 2 children)
    def test_remove_left_child_h2_IO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.remove_element(20)
        self.assertEqual("[ 15, 25, 30, 35, 40, 45 ]", self.__tree.in_order())
    
    def test_remove_left_child_h2_PRO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.remove_element(20)
        self.assertEqual("[ 30, 25, 15, 40, 35, 45 ]", self.__tree.pre_order())   
    
    def test_remove_left_child_h2_POST(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.remove_element(20)
        self.assertEqual("[ 15, 25, 35, 45, 40, 30 ]", self.__tree.post_order())      
    
    def test_remove_left_child_h2_height(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.remove_element(20)
        self.assertEqual(3, self.__tree.get_height())     
    
    ###Removal tests on perfect tree of height 3 (removing root)
    def test_remove_root_from_perfecth3_IO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.__tree.remove_element(30)
        self.assertEqual("[ 15, 20, 25, 35, 40, 45 ]", self.__tree.in_order())
    
    def test_remove_root_from_perfecth3_PRO(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.__tree.remove_element(30)        
        self.assertEqual("[ 35, 20, 15, 25, 40, 45 ]", self.__tree.pre_order())
    
    def test_remove_root_from_perfecth3_POST(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.__tree.remove_element(30)        
        self.assertEqual("[ 15, 25, 20, 45, 40, 35 ]", self.__tree.post_order())  
    
    def test_remove_root_from_perfecth3_height(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45) 
        self.__tree.remove_element(30)        
        self.assertEqual(3, self.__tree.get_height())     
        
    
if __name__ == "__main__":
    unittest.main()