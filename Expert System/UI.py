import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import pandas as pd
import numpy as np

class Interface():
    
    def __init__(self,form):
        self.form=form
        self.plants=["Apple-tree","Orange tree","Pear tree","Banana","Kiwi","Tomatoes",
                     "Potatoes","Aubergine","Cucumber","Plum","Peach","Apricot","Walnut",
                     "Almond","Carrot","Pine"]
        
        self.questions=["Is the Core Hard?",
                        "Is the Core Soft?",
                        "Is the Shell Hard?",
                        "Is the Peel Soft?",
                        "Is it an Angiosperm plant?",
                        "Is it an Angiosperm plant?",
                        "Does it bear fruit in winter?",
                        "Does it bear fruit in summer?",
                        "Does it bear fruit in spring?",
                        "Does it bear fruit in autumn?",
                        "Is his product a fruit?",
                        "Is the product a vegetable?",
                        "Is the product Acidic?",
                        "Is the product Basic?",
                        "Does it grow in a continental climate?",
                        "Does it grow in a Mediterranean climate?",
                        "Does it grow in the Black Sea climate?",
                        "Does it grow in the Marmara climate?",
                        "Does it grow underground?",
                        "Is it in the shape of a tree?",
                        "Is it in the form of a sapling?",
                        "Does the product contain vitamin A",
                        "Does the product contain vitamin C",
                        "Does the product contain vitamin E",
                        "Does the product contain vitamin K"
                        ]
        
        
        #                               Testing
        #self.asked=["Çekirdeði Sert mi?",
        #                "Çekirdeði Yumuþak mý?",
        #                "Kabuðu Sert mi?",
        #                "Kabuðu Yumuþak mý?",
        #                "Kapalý Tohumlu bir bitki mi?"]
        #self.answer=["yes",
        #             "no",
        #             "yes",
        #             "no",
        #             "yes",]
    
 
        self.Create_Window()
        self.Add_Listbox()
        self.Questions_Asked()
        print(self.Show_MessageBox(self.questions[1]))
    
    
    def Create_Window(self):
        
        self.form.geometry("1200x600")
        self.form.title("PLANT CLASSIFICATION EXPERT SYSTEM")
        
        
    def Add_Listbox(self):
        listbox=tk.Listbox(self.form,height=30)
        listbox.place(x=100,y=100)
       

        for i in range(len(self.plants)):
            listbox.insert(i,self.plants[i])
            
        # listbox.itemconfig(0, {'bg':'red'})
        # listbox.itemconfig(3, {'fg': 'blue'})


        
    def Questions_Asked(self):
        tv=ttk.Treeview(self.form)
        tv.place(x=300,y=100)
        tv["columns"]=["Questions","Answer"]
        
        for i in range(len(self.answer)):
            tv.insert(parent='', index=i,values=(self.asked[i],self.answer[i]))
        # tv.insert(parent='', index=0,  values=('1','Vineet'))
        # tv.insert(parent='', index=1,  values=('2','Anil'))

        
    def Show_MessageBox(self,message):
        if messagebox.askyesno(message=message):
            return True
        else:
            return False
        