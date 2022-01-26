'''
5. Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs cannot contain duplicate Nodes.
A BST is defined as follows:
• The left subtree of a node contains only nodes with keys less than the node's
key.
• The right subtree of a node contains only nodes with keys greater than the
node's key.
• Both the left and right subtrees must also be binary search trees.
Example:

Input: 2 / \1 3 
Output: 1 Explanation: The left subtree of root node contains node with
key lesser than the root node’s key and the right subtree of root node contains node with
key greater than the root node’s key. Hence, the tree is a BST.
'''

""" Program to check if a given Binary
Tree is balanced like a Red-Black Tree """

# Helper function that allocates a new
# node with the given data and None
# left and right poers.								
class newNode:

	# Construct to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Returns true if given tree is BST.
def isBST(root, l = None, r = None):

	# Base condition
	if (root == None) :
		return True

	# if left node exist then check it has
	# correct data or not i.e. left node's data
	# should be less than root's data
	if (l != None and root.data <= l.data) :
		return False

	# if right node exist then check it has
	# correct data or not i.e. right node's data
	# should be greater than root's data
	if (r != None and root.data >= r.data) :
		return False

	# check recursively for every node.
	return isBST(root.left, l, root) and \
		isBST(root.right, root, r)


# Driver Code
if __name__ == '__main__':
	root = newNode(2)
	root.left = newNode(1)
	root.right = newNode(3)
	#root.right.left = newNode(1)
	#root.right.right = newNode(4)
	#root.right.left.left = newNode(40)
	if (isBST(root,None,None)):
		print("Is BST")
	else:
		print("Not a BST")

'''
Time Complexity: O(n) 
Auxiliary Space: O(1) if Function Call Stack size is not considered, otherwise O(n)
'''