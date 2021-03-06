# -*- coding: utf-8 -*-
"""Answer 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zyTW9YckL1M4z3ryiawYIIM7uteOAXWa
"""

#Answer 7 (i)

import matplotlib.pyplot as plt 

# line 1 points 
x1 = [1,2,3,4,5,6] 
y1 = [2500,2630,2140,3400,3600,2760] 
# plotting the line 1 points 
plt.plot(x1, y1, label = "Toothpaste") 

# line 2 points 
x2 = [1,2,3,4,5,6]
y2 = [1500,1200,1340,1130,1740,1555] 
# plotting the line 2 points 
plt.plot(x2, y2, label = "Facewash") 

# line 3 points 
x3 = [1,2,3,4,5,6]
y3 = [5200,5100,4550,5870,4560,4890] 
# plotting the line 3 points 
plt.plot(x3, y3, label = "Shampoo") 

# line 4 points 
x4 = [1,2,3,4,5,6] 
y4 = [9200,6100,9550,8870,7760,7490] 
# plotting the line 4 points 
plt.plot(x4, y4, label = "Moisturizer")

# line 5 points 
x5 = [1,2,3,4,5,6]
y5 = [1200,2100,3550,1870,1560,1890] 
# plotting the line 5 points 
plt.plot(x5, y5, label = "Soap") 

# naming the x axis 
plt.xlabel('Month no:') 
# naming the y axis 
plt.ylabel('Sales Unit') 
# giving a title to my graph 
plt.title('') 

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show()

#Answer 7(ii)
plt.scatter(x4, y4, label = "Moisturizer Sales",color="Green")
plt.legend()
plt.show()

#Answer 7(iii)

total=[]
month=[1,2,3,4,5,6]
toothpaste=[2500,2630,2140,3400,3600,2760]  #y1
facewash =[1500,1200,1340,1130,1740,1555]    #y2
shampoo=[5200,5100,4550,5870,4560,4890]      #y3
moisturizer=[9200,6100,9550,8870,7760,7490]   #y4
soap=[1200,2100,3550,1870,1560,1890]           #y5
i=0
while i<6:
 
  total.append(toothpaste[i]+facewash[i]+shampoo[i]+moisturizer[i]+soap[i])
  i=i+1
   
# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five','six'] 
  
# plotting a bar chart 
plt.bar(month, total, tick_label = tick_label, 
        width = 0.8, color = ['pink', 'orange']) 
  
# naming the x-axis 
plt.xlabel('Month') 
# naming the y-axis 
plt.ylabel('Sales') 

  
# function to show the plot 
plt.show()