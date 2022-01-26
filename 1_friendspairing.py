'''
1. Given N friends, each one can remain single or can be paired up with some
other friend. Each friend can be paired only once. Find out the total number of
ways in which friends can remain single or can be paired up.
Note: Since answer can be very large, return your answer mod 10^9+7.

Example:

Input: N = 3 Output: 4 Explanation:{1}, {2}, {3} : All single{1}, {2,3} : 2 and 3 paired but 1
is single.{1,2}, {3} : 1 and 2 are paired but 3 is single.{1,3}, {2} : 1 and 3 are paired but 2
is single.Note that {1,2} and {2,1} are considered same.

'''
# Returns count of ways
# n people can remain
# single or paired up.
def friend(n):
 
    c = [0 for i in range(n + 1)]
 
    # Filling dp[] in bottom-up manner using
    # recursive formula explained above.
    for i in range(n + 1):
 
        if(i <= 2):
            c[i] = i
        else:
            c[i] = c[i - 1] + (i - 1) * c[i - 2]
 
    return c[n]
 
# Driver code
n = 3

print(friend(n))


''''
Time Complexity : O(n) 
Auxiliary Space : O(n)
Another approach: (Using recursion)

'''