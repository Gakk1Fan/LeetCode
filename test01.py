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


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = {value: key for key, value in enumerate(ideas)}
        d_map = collections.defaultdict(int)
        for i in range(len(ideas)):
            for j in range(i + 1, len(ideas)):
                ia, ib = ideas[i], ideas[j]
                nia = ib[0] + ia[1:]
                nib = ia[0] + ib[1:]
                iab = nia + ' ' + nib
                if nia not in d and nib not in d and iab not in d_map:
                    d_map[iab] = 1
        return len(d_map)

if __name__ == "__main__":
    a = Solution()
    """ 二叉树debug """
    root = List2Tree([2,2,2,5,2]) # 把测试用例中的 null 换成 'null'
    l1 = ["coffee","donuts","time","toffee"]
    str1 = "172.16.254.1"
    res = a.distinctNames(l1)
    print(res) 
    # 输出[[5, 4, 11, 2], [5, 8, 4, 