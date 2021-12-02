'''
class Queue: 
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1 
        self.__front = 0

    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__front>self.__rear):
            return True
        return False 

    def enqueue (self, data):                # check these conditions while we enqueue , enqueue takes data as argument
        if (self.is_full()):                 # is queue full
            print("THE QUEUE IS FULL!!!")    # only rear will get incremented in enqueue
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue (self):                      # check these conditions while we dequeue 
        if (self.is_empty()) :               #is queue empty
            print("QUEUE IS EMPTY!!")        # only front will get incremented in enqueue
        else:
            data = self.__elements[self.__front]
            self.__front += 1 
            print(data)
            return data

    def display(self):
        for index in range (self.__front , self.__rear + 1):
            print(self.__elements[index])
    
num_queue = Queue(4)

num_queue.enqueue(1)
num_queue.enqueue(2)
num_queue.enqueue(3)
num_queue.enqueue(4)
num_queue.enqueue(5)

num_queue.display()
print("\n")

num_queue.dequeue()
num_queue.dequeue()
num_queue.dequeue()
num_queue.dequeue()
num_queue.dequeue()



class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
                                       
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

    
def split_queue(num_queue):
    #Populate queue_list with odd_queue and even_queue
    queue_list=[]
    #write your logic here
    odd = []
    even = []

    while (not num_queue.is_empty()):
        i = num_queue.dequeue()
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    queue_list=[odd , even ]


    return queue_list

# Enqueue different values to the queue and test your program

num_queue=Queue(7)
num_queue.enqueue(2)
num_queue.enqueue(7)
num_queue.enqueue(9)
num_queue.enqueue(4)
num_queue.enqueue(6)
num_queue.enqueue(5)
num_queue.enqueue(10)

q_list=split_queue(num_queue)
print(q_list[0])
print(q_list[1]) 



class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
                                       
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

    
def mearge_queue(num_queue_1,num_queue_2):
    #Populate queue_list with odd_queue and even_queue
    queue_3 = Queue(num_queue_1.get_max_size() + num_queue_2.get_max_size())
    l = num_queue_1.get_max_size() + num_queue_2.get_max_size()
    print(l)
    #write your logic here
    for i in range(l):
        if not num_queue_1.is_empty():
            queue_3.enqueue(num_queue_1.dequeue())
        if not num_queue_2.is_empty():
            queue_3.enqueue(num_queue_2.dequeue())
    mearged_queue= queue_3
    return mearged_queue


    return queue_list

# Enqueue different values to the queue and test your program

num_queue_1=Queue(7)
num_queue_2=Queue(7)
num_queue_1.enqueue(2)
num_queue_1.enqueue(7)
num_queue_1.enqueue(9)
num_queue_2.enqueue(4)
num_queue_2.enqueue(6)
num_queue_2.enqueue(5)
num_queue_2.enqueue(10)


num_queue_1.display()
print("\n")
num_queue_2.display()
print("\n")
q_list=mearge_queue(num_queue_1 , num_queue_2)
print(q_list)


class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def check_numbers(number_queue):
    #write your logic here
    solution_queue1 = Queue(5)
    while(not number_queue.is_empty()):
        status = 0 
        element = number_queue.dequeue()
        for i in range(1 , 11):
            if element%i != 0:
                status = 1
                break
        if status==0:
            solution_queue1.enqueue(element)
    


    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)

q = check_numbers(number_queue)
print(q)
''' 


#          1
#      2       3
#  5      6

# inorder (left visit right):
#  5 2 6 1 3
# preorder (visit left right):
#  1 2 5 6 3 
#postorder (left right visit):
#  5 6 2 3 1
 
#       8
#    3      10              # inorder : 1 3 4 6 7 8 10 14 
# 1     6        14
#    4      7



#  BINARY SEARCH TREE 
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data 
            

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()  

# INORDER TRAVERSAL
# LEFT - VISIT - RIGHT

    def inorderTraversal(self , root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res= res + self.inorderTraversal(root.right)
            return res 
# PREORDER TRAVERSAL
# VISIT- LEFT - RIGHT


    def preorderTraversal(self , root):
        res = []
        if root:
            res.append(root.data)
            res = self.preorderTraversal(root.left)
            res= res + self.preorderTraversal(root.right)
            return res 

# POSTORDER TRAVERSAL
# LEFT - RIGHT - VISIT


    def postorderTraversal(self , root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res= res + self.postorderTraversal(root.right)
            res.append(root.data)
            return res 


                
root = Node (25)    
root.insert(78)
root.insert(43)
root.insert(25)
root.insert(54)
root.insert(12)
root.insert(00)
root.insert(167)

root.printTree()
# 25 78 43 54 12 00 167 24    
#              25              
#          12        78     
#       00    24   43    167
#                      54
#




