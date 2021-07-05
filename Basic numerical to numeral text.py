# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:14:15 2021

@author: Akash Chandra Behera
"""

#Basic numerical to text converter
#Note I used // instead of % just for fun, note % is more efficient
x=int(input("Give number pls "))
if x>10000:
    print("Error")
thous=x//1000
d = {1 : 'ONE', 2 : 'TWO', 3 : 'THREE', 4 : 'FOUR', 5 : 'FIVE', 6 : 'SIX', 7 : 'SEVEN', 8 :
'EIGHT', 9 : 'NINE'}
p = {3 : 'HUNDRED', 4 : 'THOUSAND'}


t = {2 : 'TWENTY', 3 : 'THIRTY',
4 : 'FORTY', 5 : 'FIFTY', 6 : 'SIXTY', 7 : 'SEVENTY', 8 : 'EIGHTY', 9 : 'NINETY'}

teen = {11:"ELEVEN",12:"TWELVE",13:"THIRTEEN",14:"FOURTEEN",15:"FIFTEEN",16:"SIXTEEN",17:"SEVENTEEN",
       18:"EIGHTEEN",19:"NINETEEN"}

te=[11,12,13,14,15,16,17,18,19]

if (((x%1000)%100) in te)==True:
    name=[]
    for i in d:  #This loop is to get thousands place digit
        if thous == i:
            name.append(d[i]+" "+p[4])
    for i in d: #This loop is to get hundreds place digit
        if (x-(1000*(x//1000)))//100 == i:
            name.append(d[i]+" "+p[3])
            cc=(x-(1000*(x//1000)))//100
    for i in te:
        if ((x%1000)%100)==i: #For teens
            name.append(teen[i])
    print(" ".join(name))

elif x==10000:
    print("TEN THOUSAND")
    
else:
    name=[]
    for i in d:  #This loop is to get thousands place digit
        if thous == i:
            name.append(d[i]+" "+p[4])
    for i in d: #This loop is to get hundreds place digit
        if (x-(1000*(x//1000)))//100 == i:
            name.append(d[i]+" "+p[3])
            cc=(x-(1000*(x//1000)))//100
            
    for i in t: #This loop is to get tens place digit
        if (x-(thous*1000)-(cc*100))//10==i:
            name.append(t[i])
            oo=(x-(thous*1000)-(cc*100))//10
    jo=0
    for i in d: #This loop is to get ones place digit
        if (x-(thous*1000)-(cc*100)-(oo*10))==i:
            name.append(d[i])
            
    print(" ".join(name))