def preorder(root, tree):
    if not root==".":
        print(root, end="")
        preorder(tree[root][0], tree)
        preorder(tree[root][1], tree)

def inorder(root, tree):
    if not root==".":
        inorder(tree[root][0], tree)
        print(root, end="")
        inorder(tree[root][1], tree)

def postorder(root, tree):
    if not root==".":
        postorder(tree[root][0], tree)
        postorder(tree[root][1], tree)
        print(root, end="")

N=int(input())
tree={}
for _ in range(N):
    root, left, right=input().split(" ")
    tree[root]=[left, right]

preorder('A', tree)
print("")
inorder('A', tree)
print("")
postorder('A', tree)