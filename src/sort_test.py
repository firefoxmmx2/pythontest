#!/usr/bin/env python2
#- * - coding:utf8 - * -
'''
Created on 2013-1-24

'''
from abc import ABCMeta, abstractmethod

class BaseSort:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def sort(self,array):
        pass
    def less(self,v,w): #return boolean
        return v < w
    def exch(self,array,i,j): 
        array[i],array[j] = array[j],array[i]
    def show(self,array):
        for i in array:
            print(i,)
        print()
    def isSorted(self,array): #return boolean
        for i in range(1,len(array)):
            if self.less(array[i],array[i-1]) : return False
        return True
    
class Selection(BaseSort):
    def sort(self,array):
        n = len(array)
        for i in range(n):
            min = i
            for j in range(i+1,n):
                if self.less(array[j], array[min]): min = j;
            self.exch(array,i,min)

class Insertion(BaseSort):
    def sort(self, array):
        n = len(array)
        for i in range(1,n):
            for j in range(i,0,-1):
                if not self.less(array[j], array[j-1]):
                    break
                self.exch(array, j, j-1)
                
if __name__ == '__main__':
    selection1 = Selection()
    array = [s for s in 'helloworld']
    selection1.sort(array)
    print(array)
    array = [s for s in 'helloworld']
    insertion1 = Insertion()
    insertion1.sort(array)
    print(array)