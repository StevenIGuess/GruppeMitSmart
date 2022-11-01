#!/usr/bin/env python3
import sys
def greet(values):
    for i in values:
        print("Hallo",i)
def leapyear(values):
    for i in list(map(lambda x:int(x),values)):
        if i%4==0 and bool(i%100)==bool(i%400):
            print(i,"ist ein Schaltjahr")
            continue
        print(i,"ist kein Schaltjahr")
def readContent(fileName):
    content=""
    with open(fileName,"r") as file:
        content=file.read()[:-1]
    return content
TABLE_LATEX=['"A','"O','"U','"a','"o','"u','"s']
TABLE_UTF8=["Ä","Ö","Ü","ä","ö","ü","ß"]
def utf8_to_latex(content:str):
    for i in range(7):
        content=content.replace(TABLE_UTF8[i],TABLE_LATEX[i])
    return content
def latex_to_utf8(content:str):
    for i in range(7):
        content=content.replace(TABLE_LATEX[i],TABLE_UTF8[i])
    return content
if __name__=="__main__":
    #greet(sys.argv[1:])
    leapyear(sys.argv[1:])
    #print(utf8_to_latex(readContent(sys.argv[1])))
    #print(latex_to_utf8(readContent(sys.argv[1])))