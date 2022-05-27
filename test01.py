from typing import List
import collections

#定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 将传入的数组转化为链表
def create_linked_list(arr:List):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 列表转二叉树
def List2Tree(l: List) -> TreeNode:
    """ 由输入列表生成树，返回根节点 """
    q = []
    if not l:
        return
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q:
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val=l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] != 'null':
                t.right = TreeNode(val=l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root



if __name__ == "__main__":
    a = Solution()
    """ 二叉树debug """
    root = List2Tree([2,2,2,5,2]) # 把测试用例中的 null 换成 'null'
    res = a.isUnivalTree(root)
    print(res) 
    # 输出[[5, 4, 11, 2], [5, 8, 4, 5]]