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
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.find('.') != -1 and queryIP.find(':') != -1:
            return "Neither"
        if queryIP.find('.') != -1:
            queryIP_list = queryIP.split('.')
            if len(queryIP_list) != 4:
                return "Neither"
            for item in queryIP_list:
                if len(item) == 0 or len(item) > 3:
                    return "Neither"
                if len(item) > 1 and item[0] == '0':
                    return "Neither"
                if not item.isdigit():
                    return "Neither"
                if int(item) > 255 or int(item) < 0:
                    return "Neither"
            return "IPv4"
        if queryIP.find(':') != -1:
            queryIP_list = queryIP.split(':')
            if len(queryIP_list) != 8:
                return "Neither"
            for item in queryIP_list:
                if not 1 <= len(item) <= 4:
                    return "Neither"
                if not item.isalnum():
                    return "Neither"
            return "IPv6"

if __name__ == "__main__":
    a = Solution()
    """ 二叉树debug """
    root = List2Tree([2,2,2,5,2]) # 把测试用例中的 null 换成 'null'
    str1 = "172.16.254.1"
    res = a.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334")
    print(res) 
    # 输出[[5, 4, 11, 2], [5, 8, 4, 