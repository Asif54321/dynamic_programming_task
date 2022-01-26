'''
4. Given a string S. The task is to print all permutations of a given string.
Examples:
Input: ABSG
Output:ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA
GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA
SGAB SGBA
Explanation:Given string ABSG has 24 permutations
'''

# Function to find permutations of a given string
from itertools import permutations
  
def allPermutations(str):
       
     
     permList = permutations(str)
  
     # print all permutations
     for perm in list(permList):
         print (''.join(perm))
        
# Driver program
if __name__ == "__main__":
    str = 'ABSG'
    allPermutations(str)


'''
Expected Time Complexity: O(n! * n)

Expected Space Complexity: O(n)
'''