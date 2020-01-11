N=int(input())
orders=[]
stack=[]
for _ in range(N):
    orders.append(input())
def push(num, stack):
    stack.append(num)

def top(stack):
    if len(stack)==0:
        print("-1")
    else:
        print(stack[-1])

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack)==0:
        print("1")
    else:
        print("0")

def pop(stack):
    if len(stack)==0:
        print("-1")
    else:
        print(stack[-1])
        del stack[-1]
for i in orders:
    if 'push' in i:
        push(i[5:], stack)
    if 'top' == i:
        top(stack)
    if 'pop' == i:
        pop(stack)
    if 'size' == i:
        size(stack)
    if 'empty' == i:
        empty(stack)