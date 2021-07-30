#Importing tkiner
from tkinter import*

#Importing ttk from tkinter
from tkinter import ttk

#Creating app window 
root= Tk()

#Defining tittle of the app
root.title("Tree")

#Defininig label of the app and calling geometry


root.geometry("500x700")

my_tree = ttk.Treeview(root)
# define Our Columns
my_tree['columns'] = ("Name", "Position")

#Formate our columns
my_tree.column("0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("Position", anchor=CENTER, width=80)

#Creating headings
my_tree.heading("#0", text="", anchor =W)

my_tree.heading("Name", text="Name",anchor=W)
my_tree.heading("Position", text="Position",anchor=CENTER)


# add data
my_tree.insert(parent=''  , index='end',iid=0, text="", values=("Abdul Gafar", "GrandFather" ))

my_tree.insert(parent=''  , index='end',iid=1, text="", values=("Sami Ullah", "ElderFather" ))



my_tree.insert(parent=''  , index='end',iid=2, text="", values=("Shafi Ulah", "Father" ))




#inserting child
my_tree.insert(parent=''  , index='end',iid=5, text="Child",values=("Sami Ullah","Elder Father"))
my_tree.move('5','0','0')

my_tree.insert(parent=''  , index='end',iid=6, text="Child",values=("Shafi Ullah","My Father"))
my_tree.move('6','0','0')

my_tree.insert(parent=''  , index='end',iid=7, text="Wife",values=("Kulsoom","MY Grand Mother"))
my_tree.move('7','0','0')


my_tree.insert(parent=''  , index='end',iid=9, text="",values=("Shafi Ullah","Brother"))
my_tree.move('9','1','0')

my_tree.insert(parent=''  , index='end',iid=10, text="Wife",values=("Asma","My Elder Mother"))
my_tree.move('10','1','0')


my_tree.insert(parent=''  , index='end',iid=13, text="Child",values=("Nimra Shafi","My Elder sister"))
my_tree.move('13','2','0')



my_tree.insert(parent=''  , index='end',iid=14, text="Chlid",values=("Sumaira Shafi","Me"))
my_tree.move('14','2','0')

my_tree.insert(parent=''  , index='end',iid=12, text="Wife",values=("Shahnaz Shafi","My Mother"))
my_tree.move('12','2','0')





my_tree.pack(pady=35)

root.mainloop()
