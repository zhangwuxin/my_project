#!/usr/bin/python3
#-*- coding:utf-8 -*-
# Date: 19-6-5 上午9:44
# Author:张印
# Desc：
class SingleNode:
    '''单链表的节点'''
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head==None

    def length(self):
        '''链表的长度'''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self._head
        while cur != None:
            print cur.item,
            cur = cur.next
        print ''

    def add(self,item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next!=None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
        #新节点的next指向插入位置的节点
        node.next = pre.next
        #插入位置的前一个节点的next指向新节点
        pre.next = node

    def remove(self,item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur!=None:
            if cur.item  == item:
                if not pre:
                    self._head=cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self._head
        while cur !=None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__== '__main__':
    ll=SingleLinkList()
    ll.add(2)
    ll.add(1)
    ll.append(4)
    print ll.search(4)
    ll.insert(2, 3)
    print 'length:',ll.length()
    ll.remove(1)
    ll.travel()
    ll.add(1)
    ll.travel()