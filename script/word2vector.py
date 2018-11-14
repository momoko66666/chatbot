#encoding:utf-8
import sys,os
import jieba

def tokenize(fileName):
    f = open(fileName,"r")
    line = f.readline()
    while line:
        seg_list = jieba.cut(line,cut_all=True)
        print("Full mode:"+"/".join(seg_list))

if __name__ == "__main__":
    fileName = "../data/input.txt"
    tokenize(fileName)
