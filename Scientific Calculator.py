from tkinter import *
import tkinter.messagebox as msg
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
global a,b,c,d


#===========================MAIN SCIENTIFIC CALCULATOR=============================#


def click(value):
    try:
        val = numberEntry.get()
        x = ''
    
        if value == 'C':
            val = val[0:len(val)-1]
            numberEntry.delete(0,END)
            numberEntry.insert(0,val)
            return
        elif value == 'CE':
            numberEntry.delete(0,END)

        elif value == '√':
            x = math.sqrt(eval(val))
            
        elif value == 'π':
            x = math.pi
        
        elif value == '2π':
            x = 2*math.pi
            
        elif value == 'cosθ':
            x = math.cos(math.radians(eval(val)))
            
        elif value == 'tanθ':
            x = math.tan(math.radians(eval(val)))
            
        elif value == 'sinθ':
            x = math.sin(math.radians(eval(val)))
        
        elif value == 'cosh':
            x = math.cosh(eval(val))
            
        elif value == 'tanh':
            x = math.tanh(eval(val))
            
        elif value == 'sinh':
            x = math.sinh(eval(val))

        elif value == chr(8731):
            x = eval(val)**(1/3)

        elif value =="x\u02b8":
            numberEntry.insert(END,'**')
            return
        
        elif value =="x\u00B3" :
            x = eval(val)**(3)
        
        elif value =="x\u00B2":
            x = eval(val)**(2)
        
        elif value =="ln":
            x = math.log2(eval(val))

        elif value =="deg":
            x = math.degrees(eval(val))
        
        elif value =="rad":
            x = math.radians(eval(val))
        
        elif value =="e":
            x = math.e
        
        elif value =="log₁₀":
            x = math.log10(eval(val))
        
        elif value =="x!":
            x = math.factorial(eval(val))
        
        elif value ==chr(247):
            numberEntry.insert(END,"/")
            return
        
        elif value =="=":
            x = eval(val)
        
        elif value =="(":
            numberEntry.insert(END,"(")
            return

        elif value ==")":
            numberEntry.insert(END,")")
            return
        
        elif value =="%":
            x = eval(val)*100

        else:
            numberEntry.insert(END,value)
            return
        
        numberEntry.delete(0,END)
        numberEntry.insert(0,x)
    except EXCEPTION:
        pass
    
def Exit():
    Exit = msg.askyesno("Calculater","Do you want to quit?")
    if Exit>0:
        root.destroy()
        return


#==================================MATRIX CALCULATOR========================================#


def Matrix():
    def EnterValues():
        global a,b,c,d
        R = [[],[]]
        r = rowEntry.get()
        c = colEntry.get()
        for k in r:
            row = int(k)
            R[0].append(row)
        for l in c:
            column = int(l)
            R[1].append(column)
        # R[[r,r2],[c,c2]]   
        rowvalues = valueEntry.get()
        rowvalues2 = valueEntry2.get()
        M1 = []
        M2 = []
        for i in rowvalues:
            v = int(i)
            M1.append(v)
        for j in rowvalues2:
            y = int(j)
            M2.append(y)
        a = np.array([M1])
        c = a.reshape(R[0][0], R[1][0])
        if rowvalues2 == "":
            return
        else:
            b = np.array([M2])
            d = b.reshape(R[0][1],R[1][1])
        return c,d
    def Calculations(value):
        global c, d
        try:
            if value == "Add":
                var1=np.add(c,d)
                l = ' '.join(map(str,var1))
                Output = Label(Mt, height =5, width = 15,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = l)
            if value == "Subtract":
                var1=np.subtract(c,d)
                l = ' '.join(map(str,var1))
                Output = Label(Mt, height =5, width = 15,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = l)
            if value == "DotPro":
                var1=np.dot(c,d)
                l = ' '.join(map(str,var1))
                Output = Label(Mt, height =5, width = 15,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = l)
            if value == "CrossPro":
                var1=np.cross(c,d)
                l = ' '.join(map(str,var1))
                Output = Label(Mt, height =5, width = 15,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = l)
            if value == "Determinant":
                var1=np.linalg.det(c)
                str(var1)
                Output = Label(Mt, height =5, width = 25,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = var1)
            if value == "Square":
                var1=np.square(c)
                str(var1)
                Output = Label(Mt, height =5, width = 25,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = var1)
            if value == "Transpose":
                var1=np.transpose(c)
                str(var1)
                Output = Label(Mt, height =5, width = 25,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = var1)
            if value == "Inverse":
                var1=np.linalg.inv(c)
                str(var1)
                Output = Label(Mt, height =5, width = 25,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = var1)
            if value == "Rank":
                var1=np.linalg.matrix_rank(c)
                str(var1)
                Output = Label(Mt, height =5, width = 25,font = ("comicsansms", 15,"bold"))
                Output.grid(row = 4, column=0)
                Output.config(text = var1)
        except Exception:
            pass
    Mt = Toplevel(root)
    Mt.geometry("645x500")
    Mt.resizable(width = False , height= False)
    Mt.title("Matrix Calculater")
    rows = Label(Mt , text ="Enter the number of rows for both matrices", font = ("comicsansms", 17,"bold")).grid(row = 0, column = 0)
    rowEntry = Entry(Mt, bg = "lightblue",font = ("comicsansms", 15,"bold"), borderwidth = 5 , relief = SUNKEN,width =15)
    rowEntry.grid(row = 0 ,column =1, pady = 5,padx = 3, columnspan=8)
    cols = Label(Mt , text ="Enter the number of columns for both matrices", font = ("comicsansms", 17,"bold")).grid(row = 1, column = 0)
    colEntry = Entry(Mt, bg = "lightblue",font = ("comicsansms", 15,"bold"), borderwidth = 5 , relief = SUNKEN,width =15)
    colEntry.grid(row = 1 ,column =1, pady = 5,padx = 3, columnspan=8)
    values = Label(Mt, text = "Matrix1 row values as 1234... ", font=("comicsansms", 17,"bold") ).grid(row = 2, column=0)
    valueEntry = Entry(Mt, bg = "lightblue", font = ("comicsansms", 15,"bold"), borderwidth = 5 , relief = SUNKEN,width =15)
    valueEntry.grid(row = 2 , column =1,pady = 5,padx = 3, columnspan=8)
    values2 = Label(Mt, text = "Matrix2 row values as 1234... ", font=("comicsansms", 17,"bold") ).grid(row = 3, column=0)
    valueEntry2 = Entry(Mt, bg = "lightblue", font = ("comicsansms", 15,"bold"), borderwidth = 5 , relief = SUNKEN,width =15)
    valueEntry2.grid(row = 3 , column =1,pady = 5,padx = 3, columnspan=8)
    button1 = Button(Mt,text = "Make matrix", width = 10 , height = 2, bg= "lightblue",font = ("comicsansms", 13,"bold"),borderwidth = 3 , relief = SUNKEN ,pady = 3, activebackground ="lightblue", command = EnterValues)
    button1.grid(row = 4, column = 1,columnspan=8, ipadx = 3, ipady = 1)
    calcbuttons = ["Add", "Subtract" , "DotPro", "CrossPro", "Determinant", "Transpose", "Inverse","Square","Rank"]
    columnval = 0
    rowval = 5
    for j in calcbuttons:
        button2 = Button(Mt, text = j, width = 12 , height = 4, bg= "lightblue",font = ("comicsansms", 10,"bold"),borderwidth = 3 , relief = SUNKEN ,pady = 3, activebackground ="lightblue", command = lambda button2=j:Calculations(button2))
        button2.grid(row = rowval, column = columnval,ipadx = 3 , ipady=1, padx = 3, pady = 0, sticky="NE")
        columnval += 1
        if columnval == 3:
            rowval += 1
            columnval = 0


#=====================================STATISTICS CALCULATOR=================================# 


def Stats():
    try:
        def mode():
            global m
            F = []
            c = str(Entdata.get()).split(",")
            for i in c:
                a = int(i)
                F.append(a)
            b = np.array(F)
            m = stats.mode(b)
            Lab.insert(END,m[0])
            
        def median():
            global m
            F = []
            c = str(Entdata.get()).split(",")
            for i in c:
                a = int(i)
                F.append(a)
            b = np.array([F])
            m = str(np.median(b))
            Lab.insert(END,m)
        def mean():
            global m
            F = []
            c = str(Entdata.get()).split(",")
            for i in c:
                a = int(i)
                F.append(a)
            b = np.array([F])
            m = str(np.mean(b))
            Lab.insert(END,m)
        def standard():
            global m
            F = []
            c = str(Entdata.get()).split(",")
            for i in c:
                a = int(i)
                F.append(a)
            b = np.array([F])
            m = str(np.std(b))
            Lab.insert(END,m)
        def variance():
            global m
            F = []
            c = str(Entdata.get()).split(",")
            for i in c:
                a = int(i)
                F.append(a)
            b = np.array([F])
            m = str(np.var(b))
            Lab.insert(END,m)
        def clear():
            Lab.delete('1.0',END)
    except EXCEPTION:
        pass
    
    global m
    St = Toplevel(root)
    St.geometry("455x252")
    St.resizable(width = False , height= False)  
    St.title("Stats Calculater") 
    L = Label(St, text ="Enter the data as 1,2,3", font = ("comicsansms", 17,"bold"))
    L.grid(row = 0, column = 0)
    Entdata = Entry(St, font =("comicsans", 17,"bold"),bg = "lightblue", borderwidth = 1 , relief = SUNKEN,width =12)
    Entdata.grid(row = 0, column = 1)
    Mb = Button(St, text = "Mean", font = ("comicsansms", 17,"bold"), command = mean)
    Mb.grid(row = 1, column =0, columnspan=3)
    Meb = Button(St, text = "Median", font = ("comicsansms", 17,"bold"), command = median)
    Meb.grid(row = 1, column =1,columnspan=3)
    Mob = Button(St, text = "Mode", font = ("comicsans",17,"bold"), command =mode)
    Mob.grid(row = 1, column =2, columnspan=3)
    Std = Button(St, text = "Standard Deviation", font = ("comicsans",17,"bold"), command =standard)
    Std.grid(row = 2, column =0, columnspan=7)
    Va = Button(St, text = "Variance", font = ("comicsans",17,"bold"), command =variance)
    Va.grid(row = 2, column =3, columnspan=2)
    anslabel = Label(St,text = "Result:", font = ("comicsans", 17,"bold"))
    anslabel.grid(row = 3, column =0)
    Lab = Text(St,font=("comicsans", 17,"bold"),bg = "lightblue" ,width =15, height =5)
    Lab.grid(row = 4, column =1)
    clear = Button(St,text = "Clear",font=("comicsans",17,"bold"), command = clear)
    clear.grid(row = 5, column = 1)


#==================================GRAPHS PLOTTER===================================#


def Graphs():
    try:
        def LineGraph():
            xc = []
            c = str(Xcoor.get()).split(",")
            for i in c:
                a = int(i)
                xc.append(a)
            X = np.array(xc)
            yc= []
            d = str(Ycoor.get()).split(",")
            for i in d:
                a = int(i)
                yc.append(a)
            Y = np.array(yc)
            plt.plot(X,Y)
            plt.show()
        def Histogram():
            xc = []
            c = str(Xcoor.get()).split(",")
            for i in c:
                a = int(i)
                xc.append(a)
            X = np.array(xc)
            yc= []
            d = str(Ycoor.get()).split(",")
            for i in d:
                a = int(i)
                yc.append(a)
            Y = np.array(yc)
            plt.hist(X,Y)
            plt.show()
        def Bar():
            xc = []
            c = str(Xcoor.get()).split(",")
            for i in c:
                a = int(i)
                xc.append(a)
            X = np.array(xc)
            yc= []
            d = str(Ycoor.get()).split(",")
            for i in d:
                a = int(i)
                yc.append(a)
            Y = np.array(yc)
            plt.bar(X,Y)
            plt.show()
        def Sin():
            yc = []
            c = str(Ycoor.get()).split(",")
            for i in c:
                a = int(i)
                yc.append(a)
            ang = [j*(np.pi/180) for j in yc]
            plt.plot(ang,np.sin(ang))
            plt.show()
        def Cos():
            yc = []
            c = str(Ycoor.get()).split(",")
            for i in c:
                a = int(i)
                yc.append(a)
            ang = [j*(np.pi/180) for j in yc]
            plt.plot(ang,np.cos(ang))
            plt.show()
        def Tan():
            yc = []
            c = str(Ycoor.get()).split(",")
            for i in c:
                a = int(i)
                yc.append(a)
            ang = [j*(np.pi/180) for j in yc]
            plt.plot(ang,np.tan(ang))
            plt.show()
    except EXCEPTION:
        print("Enter valid input i.e. increasing order of inputs")


    Gr = Toplevel(root)
    Gr.geometry("479x122")
    Gr.resizable(width = False , height= False)
    Gr.title("Graphs Plotter")
    Y = Label(Gr, text = "Enter the Y coordinates", font = ("comicsansms", 17,"bold"))
    Y.grid(row = 0, column = 0)
    Ycoor = Entry(Gr,font =("comicsans", 17,"bold"),bg = "lightblue", borderwidth = 1 , relief = SUNKEN,width =12)
    Ycoor.grid(row = 0, column =1)
    X = Label(Gr, text = "Enter the X coordinates", font = ("comicsansms", 17,"bold"))
    X.grid(row = 1, column = 0)
    Xcoor = Entry(Gr,font =("comicsans", 17,"bold"),bg = "lightblue", borderwidth = 1 , relief = SUNKEN,width =12)
    Xcoor.grid(row = 1, column =1)
    Line = Button(Gr, text ="Line Graph", font =("comicsans", 17,"bold"), command = LineGraph)
    Line.grid(row = 2, column =0)
    Hist = Button(Gr, text ="Histogram", font =("comicsans", 17,"bold"), command = Histogram)
    Hist.grid(row = 2,column =1)
    Bar = Button(Gr, text ="Bar Graph", font =("comicsans", 17,"bold"), command = Bar)
    Bar.grid(row = 2,column =2)
    Sine = Button(Gr, text ="Sine Graph", font =("comicsans", 17,"bold"), command = Sin)
    Sine.grid(row = 3,column =0)
    Cos = Button(Gr, text ="Cosine Graph", font =("comicsans", 17,"bold"), command = Cos)
    Cos.grid(row = 3,column =1)
    Tan = Button(Gr, text ="Tangent Graph", font =("comicsans", 17,"bold"), command = Tan)
    Tan.grid(row = 3,column =2)



#==============================LINEAR EQUATION CALCULATOR====================================#


def LinearEq():
    def cals():
        try:
            x1 = eval(Ent1.get())
            y1 = eval(Ent2.get())
            z1 = eval(Ent3.get())
            x2 = eval(Ent5.get())
            y2 = eval(Ent6.get())
            z2 = eval(Ent7.get())
            x3 = eval(Ent9.get())
            y3 = eval(Ent10.get())
            z3 = eval(Ent11.get())
            rhs1 = eval(Ent4.get())
            rhs2 = eval(Ent8.get())
            rhs3 = eval(Ent12.get())
            eq1 = [x1,y1,z1]
            eq2 = [x2,y2,z2]
            eq3 = [x3,y3,z3]
            rhs = [rhs1,rhs2,rhs3]
            A = np.array([eq1, eq2, eq3])
            B = np.array(rhs)
            ans = np.linalg.solve(A, B)
            Ent13.insert(0,str(ans[0]))
            Ent14.insert(0,str(ans[1]))
            Ent15.insert(0,str(ans[2]))
        except Exception:
            pass

    Le = Toplevel(root)
    Le.geometry("575x262")
    Le.resizable(width = False , height= False)
    Le.title("Linear Equations Calculator")
    Eq1 = Label(Le, text = "Equation1",font = ("comicsansms", 17,"bold"))
    Eq1.grid(row = 0, column = 0)
    Ent1 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent1.grid(row = 1, column =0)
    X = Label(Le, text = "X",font = ("comicsansms", 17,"bold"))
    X.grid(row = 1, column = 1)
    Ent2 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent2.grid(row = 1, column =2)
    Y = Label(Le, text = "Y",font = ("comicsansms", 17,"bold"))
    Y.grid(row = 1, column = 3)
    Ent3 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent3.grid(row = 1, column =4)
    Z = Label(Le, text = "Z =",font = ("comicsansms", 17,"bold"))
    Z.grid(row = 1, column = 5)
    Ent4 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent4.grid(row = 1, column =6)
    
    Eq2 = Label(Le, text = "Equation2",font = ("comicsansms", 17,"bold"))
    Eq2.grid(row = 2, column = 0)
    Ent5 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent5.grid(row = 3, column =0)
    X2 = Label(Le, text = "X",font = ("comicsansms", 17,"bold"))
    X2.grid(row = 3, column = 1)
    Ent6 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent6.grid(row = 3, column =2)
    Y2 = Label(Le, text = "Y",font = ("comicsansms", 17,"bold"))
    Y2.grid(row = 3, column = 3)
    Ent7 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent7.grid(row = 3, column =4)
    Z2 = Label(Le, text = "Z =",font = ("comicsansms", 17,"bold"))
    Z2.grid(row = 3, column = 5)
    Ent8 = Entry(Le, bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent8.grid(row = 3, column =6)
    
    Eq3 = Label(Le, text = "Equation3",font = ("comicsansms", 17,"bold"))
    Eq3.grid(row = 4, column = 0)
    Ent9 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent9.grid(row = 5, column =0)
    X3 = Label(Le, text = "X",font = ("comicsansms", 17,"bold"))
    X3.grid(row = 5, column = 1)
    Ent10 = Entry(Le, bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent10.grid(row = 5, column =2)
    Y3 = Label(Le, text = "Y",font = ("comicsansms", 17,"bold"))
    Y3.grid(row = 5, column = 3)
    Ent11 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent11.grid(row = 5, column =4)
    Z3 = Label(Le, text = "Z =",font = ("comicsansms", 17,"bold"))
    Z3.grid(row = 5, column = 5)
    Ent12 = Entry(Le, bg = "lightblue", font = ("comicsansms", 17,"bold"), borderwidth = 1 , relief = SUNKEN,width =10)
    Ent12.grid(row = 5, column =6)

    solve = Button(Le,text = "Solve", width = 15 , height = 3, bg= "lightblue",font = ("comicsansms", 10,"bold"),borderwidth = 1 , relief = SUNKEN ,pady = 3, command = cals)
    solve.grid(row = 6, column = 0)

    result = Label(Le, text = "Result:",font = ("comicsansms", 17,"bold"))
    result.grid(row = 7, column =0)
    ansx = Label(Le, text = "X:",font = ("comicsansms", 17,"bold"))
    ansx.grid(row = 7, column =1)
    Ent13 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"),borderwidth = 1 , relief = SUNKEN,width =10)
    Ent13.grid(row=7, column =2)
    ansy = Label(Le, text = "Y:",font = ("comicsansms", 17,"bold"))
    ansy.grid(row = 7, column =3)
    Ent14 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"),borderwidth = 1 , relief = SUNKEN,width =10)
    Ent14.grid(row=7, column =4)
    ansz = Label(Le, text = "Z:",font = ("comicsansms", 17,"bold"))
    ansz.grid(row = 7, column =5)
    Ent15 = Entry(Le,bg = "lightblue", font = ("comicsansms", 17,"bold"),borderwidth = 1 , relief = SUNKEN,width =10)
    Ent15.grid(row=7, column =6)



root = Tk()
root.geometry("625x462")
root.resizable(width = False , height= False)
root.title("Scientific Calculater")


calc = Frame(root)
calc.grid(row = 0, column =0)
menubar = Menu(calc)
typemenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Type", menu = typemenu)
typemenu.add_command(label ="Matrix Calculater" ,command = Matrix)
typemenu.add_command(label ="Statistics Calculater", command = Stats)
typemenu.add_command(label ="Graph Plotter", command=Graphs)
typemenu.add_command(label ="Linear Equations Calulator", command=LinearEq)
typemenu.add_separator()
typemenu.add_command(label = "Exit", command = Exit)
root.config(menu = menubar)

numberEntry = Entry(root, bg = "lightblue", font = ("comicsansms", 35,"bold"), borderwidth = 5 , relief = SUNKEN,width =25)
numberEntry.grid(row = 1, column =0, pady = 5,padx = 3, columnspan=8)
theButtons = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
              "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
              "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
              "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
              "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
colvalue = 0
rowvalue = 2
for i in theButtons:
    button = Button(root, text = i, width = 5 , height = 3, bg= "lightblue",font = ("comicsansms", 20,"bold"),borderwidth = 3 , relief = SUNKEN ,pady = 3, activebackground ="lightblue", command = lambda button=i:click(button))
    button.grid(row = rowvalue, column = colvalue)
    colvalue += 1
    if colvalue == 8:
        rowvalue += 1
        colvalue = 0

root.mainloop()