import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

Data=np.array([['a','b','c','d',1,2,3,4,5,'j'],['c','d','e','f',1,2,3,4,5,'b']])
class Gui:
def __init__(self,Data):
root=Tk()
root.title('find player')
self.root=root
self.Data=Data
self.box=Data
self.hikaru=False


def plot_graph(self,index1):
index1=index1[0]
list_match_before=['5 day','4 day','3 day','2 day','1 day']
list_form=[float(i) for i in self.Data[index1,4:9]]
plt.title('Form')
plt.plot(list_match_before,list_form,label='Form before match',color='blue')
plt.xlabel('Before match')
plt.ylabel('Form')
plt.legend(loc='best')
plt.show()


def New_root(self,team,name,index1):
root2=Tk()
root2.title('Information of player')
Label(root2,text='Information',font=20).grid(row=0,column=0,sticky=W)
Label(root2,text='Name : '+name,font=15).grid(row=1,sticky=W)
Label(root2,text='Team : '+team,font=15).grid(row=2,sticky=W)
Label(root2,text='Age : '+self.Data[index1[0],2],font=15).grid(row=3,sticky=W)
Label(root2,text='Market value(EUR) : '+self.Data[index1[0],3],font=15).grid(row=4,sticky=W)
Label(root2,text='Average form : '+self.Data[index1[0],9],font=15).grid(row=5,sticky=W)
self.plot_graph(index1)
root2.mainloop()

def delete(self):
self.hikaru=False
self.frontend()

def research(self,team,name):
name=name.get()
team=team.get()
index1=np.argwhere(self.Data[:,0]==name).ravel()
index2=np.argwhere(self.Data[:,1]==team).ravel()
list_accurate=[]
if len(index1)==0 and len(index2)!=0 :
self.hikaru=True
amount=len(name)
for i in index2:
count=0
for j in range(amount):
if j>=len(self.Data[i,0]):
break
if self.Data[i,0][j]==name[j]:
count+=1
accurate=(count/amount)*100
list_accurate.append(accurate)
best_accurate=sorted(list_accurate,reverse=True)[0]
list_best_accurate=np.argwhere(list_accurate==best_accurate)
box=tuple(self.Data[list_best_accurate,0])
self.box=box
self.team=team
self.name=name
self.frontend()
elif len(index1)==0 and len(index2)==0:
self.hikaru=True
amount=len(name)
for i in range(self.Data.shape[0]):
count=0
for j in range(amount):
if j>=len(self.Data[i,0]):
break
if self.Data[i,0][j]==name[j]:
count+=1
accurate=(count/amount)*100
list_accurate.append(accurate)
best_accurate=sorted(list_accurate,reverse=True)[0]
list_best_accurate=np.argwhere(list_accurate==best_accurate)
box=tuple(self.Data[list_best_accurate,0])
self.box=box
self.team=team
self.name=name
self.frontend()
elif len(index1)!=0 and len(index2)!=0:
self.New_root(team,name,index1)
elif len(index1)!=0 and len(index2)!=0:
self.New_root(team,name,index1)











def frontend(self):
if self.hikaru==False:
team=StringVar(value='Choose team')
Label(self.root,text='Team : ',font=20).grid(row=0,sticky=W)
combo1=ttk.Combobox(self.root,width=30,font=20,textvariable=team)
combo1['values']=tuple(self.Data[:,1])
combo1.grid(row=0,column=1)


name=StringVar(value='Choose player')
Label(self.root,text='Name : ',font=20).grid(row=1,sticky=W)
combo2=ttk.Combobox(self.root,font=20,width=30,textvariable=name)
combo2['values']=tuple(self.Data[:,0])
combo2.grid(row=1,column=1)

btn1=Button(self.root,text='search',width=15,font=10,bg='red',command=lambda:self.research(team,name)).grid(row=2,column=1,sticky=W)
btn2=Button(self.root,text='clear',width=15,font=10,bg='blue',command=self.delete).grid(row=2,column=1,sticky=E)
self.root.mainloop()
else:
team=StringVar(value=self.team)
Label(self.root,text='Team : ',font=20).grid(row=0,sticky=W)
combo1=ttk.Combobox(self.root,width=30,font=20,textvariable=team)
combo1['values']=tuple(self.Data[:,1])
combo1.grid(row=0,column=1)


name=StringVar(value=self.name)
Label(self.root,text='Name : ',font=20).grid(row=1,sticky=W)
combo2=ttk.Combobox(self.root,font=20,width=30,textvariable=name)
combo2['values']=tuple(self.box)
combo2.grid(row=1,column=1)

btn1=Button(self.root,text='search',width=15,font=10,bg='red',command=lambda:self.research(team,name)).grid(row=2,column=1,sticky=W)
btn2=Button(self.root,text='clear',width=15,font=10,bg='blue',command=self.delete).grid(row=2,column=1,sticky=E)
self.root.mainloop()






a=Gui(Data)
a.frontend()
