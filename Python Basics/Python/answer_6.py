# -*- coding: utf-8 -*-
"""Answer 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yXJTob2Kw_0Vio3nUWzhfF1St5qu02U4
"""

#Ans:6
list_one=[]
list_two=[]
list_three=[]
list_four=[]
final_list=[]
i=0
n = int(input("Number of element for List One:"))
print("Enter List One Element :")
while i < n:
  list_one.append(int(input()))         #input list one
  i=i+1
 
n=0
i=0
n = int(input("Number of element for List two:"))
print("Enter List two Element :")
while i < n:
  list_two.append(int(input()))             #input list two   
  i=i+1



#list_one[1::2] means range selection between 1 and len(L) with step 2. That is, select 1st, 3rd, 5th, …, and so on

list_three=list_one[1::2] 
print("Calculate Element at odd-index positions from list one",list_three)

#list_two[::2] means range selection between 0 and len(L) with step 2. That is, select 0th, 2nd, 4th, …, and so on.
list_four=list_two[::2] 
print("Calculate Element at even-index positions from list one",list_four)



final_list=list_three+list_four #Final updated list
print("Printing Final third list",final_list)