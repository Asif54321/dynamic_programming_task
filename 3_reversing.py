'''
3. Given an integer K and a queue of integers, we need to reverse the order of
the first K elements of the queue, leaving the other elements in the same relative
order.
Only following standard operations are allowed on queue.
• enqueue(x) : Add an item x to rear of queue
• dequeue() : Remove an item from front of queue
• size() : Returns number of elements in queue.
• front() : Finds front item.
Example:

Input:5 31 2 3 4 5Output: 3 2 1 4 5Explanation: After reversing the given input from the 3rd
position the resultant output will be 3 2 1 4 5.
'''

from queue import Queue
 
# Function to reverse the first K
# elements of the Queue
def reverseQueueFirstKElements(k, Queue):
    if (Queue.empty() == True or
             k > Queue.qsize()):
        return
    if (k <= 0):
        return
 
    Stack = []
 
    # put the first K elements
    # into a Stack
    for i in range(k):
        Stack.append(Queue.queue[0])
        Queue.get()
 
    # Enqueue the contents of stack
    # at the back of the queue
    while (len(Stack) != 0 ):
        Queue.put(Stack[-1])
        Stack.pop()
 
    # Remove the remaining elements and
    # enqueue them at the end of the Queue
    for i in range(Queue.qsize() - k):
        Queue.put(Queue.queue[0])
        Queue.get()
 
# Utility Function to print the Queue
def Print(Queue):
    while (not Queue.empty()):
        print(Queue.queue[0], end =" ")
        Queue.get()
 
# Driver code

if __name__ == '__main__':
    Queue = Queue()
    Queue.put(1)
    Queue.put(2)
    Queue.put(3)
    Queue.put(4)
    Queue.put(5)
 
    k = 3
    reverseQueueFirstKElements(k, Queue)
    Print(Queue)

'''
Time Complexity: O(n+k). 
Where ‘n’ is the total number of elements in the queue and ‘k’ is the number of elements to be reversed. 
This is because firstly the whole queue is emptied into the stack and after that first
‘k’ elements are emptied and enqueued in the same way.
Auxiliary Space :Use of stack to store values for the purpose of reversing-: O(n)
'''