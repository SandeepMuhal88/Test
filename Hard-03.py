# .Implement Queue without using inbuilt function ?
# Queue 
# enque
# dequeue
# display
# Size

queue=[]
def enquee(element):
    queue.append(element)

def size():
    print(len(queue))

def display():
    print("The Queue is :-",queue)

def is_empty():
    if len(queue)==0:
        print("Queue is Empty")
    else:
        print("Queue is Not empty")
def dequeue():
    queue.pop()
