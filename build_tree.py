#!usr/bin/python
# _*_ coding:utf-8 _*_

from Node import Node
import codecs

# define find children function
def find_children(parent, MaxLength, WordGradeDict):
    '''find the children node for a given parent node.'''
    pL = len(parent.value)
    for i in range(pL+1, MaxLength+1):
        tmpList = WordGradeDict['WList{}'.format(i)]
        for node in tmpList:
            if parent < node:
                parent.add_children(node)
                node.is_root = False

def DFS_Print(PathStack, node):
    PathStack.append(node)
    if len(node.children) == 0:
        WritePath(PathStack)
        PathStack.pop()
        return
    for ele in node.children:
        DFS_Print(PathStack, ele)
    PathStack.pop()

def WritePath(PathStack):
    global f
    ValueStack = map(lambda x:x.value, PathStack)
    f.write('-->'.join(ValueStack))
    f.write('\r\n')

def main():
    # read from file
    with codecs.open('word_repository.txt', encoding='utf-8') as f:
        WordList = map(lambda x:x.strip(), f.readlines())
    MaxLength = max(map(len,WordList))
    # build as a graded dict
    WordGradeDict = {}
    for i in range(1, MaxLength+1):
        WordGradeDict['WList{}'.format(i)] = []
    for ele in WordList:
        WordGradeDict['WList{}'.format(len(ele))].append(Node(ele))
    # build tree
    for i in range(1, MaxLength+1):
        tmpList = WordGradeDict['WList{}'.format(i)]
        for ele in tmpList:
            find_children(ele, MaxLength, WordGradeDict)
    # DFS algorithm
    PathStack = []
    for i in range(1, MaxLength+1):
        tmpList = WordGradeDict['WList{}'.format(i)]
        for ele in tmpList:
            if ele.is_root:
                DFS_Print(PathStack, ele)
if __name__=="__main__":
    with codecs.open('word_forest.txt','wb',encoding='utf-8') as f:
        main()
