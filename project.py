import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

Data = pd.read_csv('kiki.csv')   #อ่านไฟล์
Data=Data.values
class Gui:              #backend front stored in class
    def __init__(self,Data):  #หน้าต่าง
        root=Tk()
        root.title('find player')
        self.root=root
        self.Data=Data
        self.box=Data
        self.hikaru=False

    def exchange(self,gg):  #add , 
        exchange=''
        count=0
        for i in range(-1,-len(str(gg))-1,-1):
            if count==2:
                exchange=','+str(gg)[i]+exchange
                count=0
            else:
                exchange=str(gg)[i]+exchange
                count+=1
        print(exchange)        
        return exchange        



    def plot_graph(self,index1): #mat plot show performance graph
        index1=index1[0]
        list_match_before=['5 match','4 match','3 match','2 match','1 match']
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
        Label(root2,text='Team : '+self.Data[index1[0],1],font=15).grid(row=2,sticky=W) #ตําเเหน่งเเถวในข้อมูล
        Label(root2,text='Age : '+str(self.Data[index1[0],2]),font=15).grid(row=3,sticky=W)
        Label(root2,text='Market value(EUR) : '+str(self.Data[index1[0],3]),font=15).grid(row=4,sticky=W)
        Label(root2,text='Average form : '+str(self.Data[index1[0],9]),font=15).grid(row=5,sticky=W)
        co=float(''.join(self.Data[index1[0],3].split(','))) #remove ,
        if self.Data[index1[0],2]<=20:
            if 6<=self.Data[index1[0],9]<6.5:
                gg=co*1.2
            elif 6.5<=self.Data[index1[0],9]<7:
                gg=co*1.25 
            elif 7<=self.Data[index1[0],9]<7.5:
                gg=co*1.3      
            elif 8<=self.Data[index1[0],9]<8.5:
                gg=co*1.35  
            elif 9<=self.Data[index1[0],9]<9.5:
                gg=co*1.4
            else:
                gg=co
            v=self.exchange(int(gg))    
            Label(root2,text='Market value(EUR) next year: '+str(v),font=20).grid(row=6,sticky=W) 
        elif self.Data[index1[0],2]<=24:
            if 6<=self.Data[index1[0],9]<6.5:
                gg=co*1.15
            elif 6.5<=self.Data[index1[0],9]<7:
                gg=co*1.2 
            elif 7<=self.Data[index1[0],9]<7.5:
                gg=co*1.25     
            elif 8<=self.Data[index1[0],9]<8.5:
                gg=co*1.3 
            elif 9<=self.Data[index1[0],9]<9.5:
                gg=co*1.35
            else:
                gg=co
            v=self.exchange(int(gg))      
            Label(root2,text='Market value(EUR) next year: '+str(v),font=20).grid(row=6,sticky=W) 
        elif self.Data[index1[0],2]<=29:
            if 6<=self.Data[index1[0],9]<6.5:
                gg=co*1.1
            elif 6.5<=self.Data[index1[0],9]<7:
                gg=co*1.15
            elif 7<=self.Data[index1[0],9]<7.5:
                gg=co*1.2     
            elif 8<=self.Data[index1[0],9]<8.5:
                gg=co*1.25 
            elif 9<=self.Data[index1[0],9]<9.5:
                gg=co*1.3
            else:
                gg=co
            v=self.exchange(int(gg))      
            Label(root2,text='Market value(EUR) next year: '+str(v),font=20).grid(row=6,sticky=W)        
        elif self.Data[index1[0],2]<=32:
            if 6<=self.Data[index1[0],9]<6.5:
                gg=co*0.85
            elif 6.5<=self.Data[index1[0],9]<7:
                gg=co*0.95
            elif 7<=self.Data[index1[0],9]<7.5:
                gg=co*1.05   
            elif 8<=self.Data[index1[0],9]<8.5:
                gg=co*1.15 
            elif 9<=self.Data[index1[0],9]<9.5:
                gg=co*1.25
            else:
                gg=co
            v=self.exchange(int(gg))      
            Label(root2,text='Market value(EUR) next year: '+str(v),font=20).grid(row=6,sticky=W)   
        elif self.Data[index1[0],2]>=32:
            if 6<=self.Data[index1[0],9]<6.5:
                gg=co*0.85
            elif 6.5<=self.Data[index1[0],9]<7:
                gg=co*0.9
            elif 7<=self.Data[index1[0],9]<7.5:
                gg=co*1   
            elif 8<=self.Data[index1[0],9]<8.5:
                gg=co*1.1
            elif 9<=self.Data[index1[0],9]<9.5:
                gg=co*1.2
            else:
                gg=co 
            v=self.exchange(int(gg))     
            Label(root2,text='Market value(EUR) next year: '+str(v),font=20).grid(row=6,sticky=W)           
        self.plot_graph(index1) # pop up thr graph before info
        root2.mainloop()
      
    def delete(self): #back to front end when clear
        self.hikaru=False
        self.frontend()    

    def research(self,team,name):
        name=name.get() #เอาข้อมูลออกจากname string var
        team=team.get()
        index1=np.argwhere(self.Data[:,0]==name).ravel() #หาชื่อเเละเจอเลย
        index2=np.argwhere(self.Data[:,1]==team).ravel() #หาteamเเละเจอเลย
        list_accurate=[]
        if len(index1)==0 and len(index2)!=0 : #เจอทีมเเต่ไม่เจอชื้อจะให้listทุกคนมา หรือให้ความใกล้เคียงกับที่พิม  
            self.hikaru=True
            amount=len(name)
            if amount==0:
                list_1=[]    
                for i in index2:
                    list_1.append(self.Data[i,0])
                box=tuple(list_1)    
            else:        
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
                list_best_accurate=np.argwhere(np.array(list_accurate)==best_accurate)
                box=tuple(self.Data[index2[list_best_accurate.ravel()],0])
            self.box=box
            self.team=team
            self.name=name
            self.frontend()  #back to front end
        elif len(index1)==0 and len(index2)==0:    #cannot find team and player program find most similar name fromall team
            self.hikaru=True
            amount=len(name)
            if amount==0:
                box=tuple(self.Data[:,0])
            else:
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
                    list_best_accurate=np.argwhere(np.array(list_accurate)==best_accurate)
                    box=tuple(self.Data[list_best_accurate.ravel(),0])
            self.box=box
            self.team=team
            self.name=name     
            self.frontend()
        elif len(index1)!=0 and len(index2)==0:   #can find name but not team  execute program
            self.New_root(team,name,index1)   #pop up New_root 
        elif len(index1)!=0 and len(index2)!=0:  #find both team and name 
            self.New_root(team,name,index1)    





            





    def frontend(self):
        if self.hikaru==False:   
            team=StringVar(value='Choose team') #ตัวเเปรที่เอาไว้เก็บข้อมูลเวลาที่ผู้ใช้งานเก็บเข้ามา
            Label(self.root,text='Team : ',font=20).grid(row=0,sticky=W)    
            combo1=ttk.Combobox(self.root,width=30,font=20,textvariable=team) #ตอนที่พิมชื่อเเล้วขึ้น
            combo1['values']=tuple(np.unique(self.Data[:,1])) #ดูชื่อในbox
            combo1.grid(row=0,column=1) 


            name=StringVar(value='Choose player')
            Label(self.root,text='Name : ',font=20).grid(row=1,sticky=W)
            combo2=ttk.Combobox(self.root,font=20,width=30,textvariable=name)
            combo2['values']=tuple(self.Data[:,0])
            combo2.grid(row=1,column=1)

            btn1=Button(self.root,text='search',width=15,font=10,bg='red',command=lambda:self.research(team,name)).grid(row=2,column=1,sticky=W)
            btn2=Button(self.root,text='clear',width=15,font=10,bg='blue',command=self.delete).grid(row=2,column=1,sticky=E)
            self.root.mainloop()  #red blue buttons
        else: # ข้อความจะเปลียนเป็นที่กรอก
            team=StringVar(value=self.team)
            Label(self.root,text='Team : ',font=20).grid(row=0,sticky=W)    
            combo1=ttk.Combobox(self.root,width=30,font=20,textvariable=team)
            combo1['values']=tuple(np.unique(self.Data[:,1]))
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

