import re
import matplotlib.pyplot as plt
import matplotlib
import CassandraClass
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from tkinter import Label
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Button
from tkinter import Frame


class MainView:
    #def __init__(self,cassandrainstance):
    def __init__(self,clusterlist):




        cassandraclusterinstance=clusterlist['folder1']
        
        #taking last node...to be improved
        for k in cassandraclusterinstance.listcassandranode.keys():
            self.cassandrainstance=cassandraclusterinstance.listcassandranode[k]
        
        root = Tk.Tk()
        #root.attributes('-fullscreen',True)
        root.wm_title("Embedding in TK 2")

        #topmenuframe=Frame(root)
        #topmenuframe.pack()

        #bottommenuframe=Frame(root)
        #bottommenuframe.pack()

        leftmenuframe=Frame(root)
        leftmenuframe.pack(side=Tk.LEFT)

        rightmenuframe=Frame(root)
        rightmenuframe.pack(side=Tk.RIGHT)

        topleftmenuframe=Frame(leftmenuframe)
        topleftmenuframe.pack(side=Tk.TOP)

        toprightmenuframe=Frame(rightmenuframe)
        toprightmenuframe.pack(side=Tk.TOP)

        bottomleftmenuframe=Frame(leftmenuframe)
        bottomleftmenuframe.pack(side=Tk.BOTTOM,fill=Tk.BOTH, expand=1)

        bottomrightmenuframe=Frame(rightmenuframe)
        bottomrightmenuframe.pack(side=Tk.BOTTOM,fill=Tk.BOTH, expand=1)

        




        #displaying keyspace data for fun in a pie




        
        
        self.datakeyspace=self.cassandrainstance.listkeyspace[3]

        labels=[]
        sizes=[]
        explode=[]

        for l in self.datakeyspace.listtable:
            if l.spaceusedtotal!="0":
                labels.append(l.name)
                sizes.append(l.spaceusedtotal)
                explode.append(0)

        #explode = (0, 0.1, 0, 0)

        #print("here are sizes: ")
        #print(sizes)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        #plt.show()

        #more display
        labels=[]
        sizes=[]
        indice=[]
        i=0

        for l in self.datakeyspace.listtable:
            if l.localwritelatency!="0":
                labels.append(l.name)
                sizes.append(float(l.localwritelatency)*1000)
                indice.append(i)
                i=i+1


        fig2, ax2 = plt.subplots()
        ##ax2.barh(indice, sizes, tick_label=labels)
        #ax2.barh(indice, sizes)
        #ax2.set_yticklabels(labels)
                
       


        # a tk.DrawingArea
        w = Label(topleftmenuframe, text="*** Data shown per table for specific node ****")
        w.pack(side=Tk.TOP)

        #show cluster
        #variablecluster = StringVar(root)
        #variablecluster.set("folder") # default value

        #w5 = OptionMenu(topleftmenuframe, variablecluster, *list(clusterlist.keys()))
        #w5.pack(side=Tk.TOP)

        
        #show
        
        nodemenuframe=Frame(topleftmenuframe)
        nodemenuframe.pack()

        variablefile = StringVar(root)
        variablefile.set("Choose node") # default value

        w4 = OptionMenu(nodemenuframe, variablefile, *list(cassandraclusterinstance.listcassandranode.keys()))
        w4.pack(side=Tk.LEFT)


        #def changenode():
            ##cassandrainstance=cassandraclusterinstance.listcassandranode
            #print("value:"+variablefile.get())
            ##self.cassandrainstance=variable.get()
            
            #self.cassandrainstance=cassandraclusterinstance.listcassandranode[variablefile.get()]

            #self.datakeyspace=self.cassandrainstance.listkeyspace[3]

        #buttonnodechoice = Button(nodemenuframe, text="Validate node", command=changenode)
        #buttonnodechoice.pack(side=Tk.RIGHT)

        
        propertymenuframe=Frame(topleftmenuframe)
        propertymenuframe.pack()
        
        variable = StringVar(root)
        variable.set("Choose property") # default value

        w3 = OptionMenu(propertymenuframe, variable, *list(self.cassandrainstance.listkeyspace[-1].listtable[-1].data.keys()))
        w3.pack(side=Tk.LEFT)


        #testing drop down
        def ok():

            #getting node choosen
            print("value:"+variablefile.get())
            self.cassandrainstance=cassandraclusterinstance.listcassandranode[variablefile.get()]
            self.datakeyspace=self.cassandrainstance.listkeyspace[3]
            
            ax1.clear()
            tmpmap={}
            #test

            tmpmap=self.cassandrainstance.listkeyspace[-2].get_tablecolumnvalue(variable.get())
            tmplabels=[]
            tmpsizes=[]
            tmpexplode=[]
            
            for row in tmpmap:
                tmplabels.append(row)
                tmpsizes.append(tmpmap[row])
                tmpexplode.append(0)

            #print("len of tmpsizes is:"+str(len(tmpsizes)))
            #print("len of tmpexplode is:"+str(len(tmpexplode)))


            ax1.pie(tmpsizes,explode=tmpexplode ,labels=tmplabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
            canvas.draw()
            #root.quit(side=Tk.TOP)
            

        button = Button(propertymenuframe, text="OK", command=ok)
        button.pack(side=Tk.RIGHT)


        canvas = FigureCanvasTkAgg(fig1, master=bottomleftmenuframe)
        canvas.show()
        canvas.get_tk_widget().pack(fill=Tk.BOTH, expand=1)

        w6 = Label(toprightmenuframe, text="**** Data shown for a specific table in the whole cluster *****")
        w6.pack(side=Tk.TOP)

        variabletable = StringVar(root)
        variabletable.set("Choose table") # default value

        tmplistable={}
        for i in self.cassandrainstance.listkeyspace[-2].listtable:
            tmplistable[i.name]=i
           
        
        w7 = OptionMenu(toprightmenuframe, variabletable, *list(tmplistable))
        w7.pack(side=Tk.TOP)

        variabledata2 = StringVar(root)
        variabledata2.set("Choose property") # default value

        w8 = OptionMenu(toprightmenuframe, variabledata2, *list(self.cassandrainstance.listkeyspace[-1].listtable[-1].data.keys()))
        w8.pack(side=Tk.TOP)

        #too much code in the view here
        def clusterdisplay():
            ax2.clear()
            tmpresult={}
            
            tmplabels=[]
            tmpsizes=[]
            tmpexplode=[]

            
            print('ca va')
            print(variabletable.get())
            print(variabledata2.get())
            for k in cassandraclusterinstance.listcassandranode.keys():
                print('name'+k)
                l=cassandraclusterinstance.listcassandranode[k]
                #for m in l.listkeyspace:
                    #print('name keyspace'+m.name)

                #hardcoding to refer to the data keyspace...not good
                n=l.listkeyspace[-2]
                print('working on keyspace'+n.name)
                for o in n.listtable:
                    #print('list of table'+o.name)
                    if o.name==variabletable.get():
                        #print('victory, we check table:'+o.name)
                        tmpresult[k]=o.data[variabledata2.get()]
                    
            for p in tmpresult:
                print(p)
                tmplabels.append(p)
                tmpsizes.append(tmpresult[p])
                tmpexplode.append(0)

            #for q in tmplabels:
                #print("label is"+q)

            #for r in tmpsizes:
                #print("value is"+str(r))

            ax2.pie(tmpsizes,explode=tmpexplode ,labels=tmplabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
            canvas2.draw()

                
                

                

        buttonnodechoice = Button(toprightmenuframe, text="ok", command=clusterdisplay)
        buttonnodechoice.pack(side=Tk.RIGHT)


        

        canvas2 = FigureCanvasTkAgg(fig2, master=bottomrightmenuframe)
        canvas2.show()
        canvas2.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, bottomrightmenuframe)
        toolbar.update()
        #canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        button = Tk.Button(master=bottomrightmenuframe, text='Quit', command=_quit)
        button.pack(side=Tk.BOTTOM)

        #plt.draw()

        Tk.mainloop()
