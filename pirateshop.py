from tkinter import *
from tkinter.ttk import *
#Comment out the line below if not on MacOSX
from tkmacosx import Button, DictVar
import tkinter.font as font

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

w = Tk()
w.title('Pirate Shop')

pirateFont1 = font.Font(family ='Trattatello', size=20)
pirateFont2 = font.Font(family ='Lucida Blackletter', size=40)
pirateFont3 = font.Font(family ='Apple Chancery', size=20)
pirateFont4 = font.Font(family ='Baskerville Old Face', size=20)
pirateFont5 = font.Font(family ='Cooper Black', size=20)
pirateFont6 = font.Font(family ='Edwardian Script ITC', size=20)
pirateFont7 = font.Font(family ='Goudy Old Style', size=20)
pirateFont8 = font.Font(family ='Kokonor', size=20)
pirateFont9 = font.Font(family ='Monotype Corsiva', size=20)
pirateFont10 = font.Font(family ='Zapfino', size=20)
pirateFont11 = font.Font(family ='Snell Roundhand', size=20)
pirateFont12 = font.Font(family ='Savoye LET', size=20)


item_prices = {'Pegleg': '☩',
               'Eyepatch': '☩',
               'Hook': '☩',
               'Parrot': '☩',
               'Cutlass': '☩',
               'Blunderbuss': '☩',
               'Musket': '☩',
               'Gunpowder': '☩',
               'Cannonball': '☩',
               'Cannon': '☩',
               'Jolly Roger': '☩',
               'Bottle of Rum': '☩',
               'Barrel of Rum': '☩',
               'Treasure Map': '☩',
               'Treasure Chest': '☩',
               'Tricorne': '☩',
               'Spyglass': '☩',
               'Accordion': '☩',
               'Compass': '☩',
               'Pipe': '☩',
               'Tobacco': '☩',
               'Long Johns': '☩',
               'Jabot': '☩',
               'Bandana': '☩',
               'Plank': '☩',
               'Anchor': '☩',
               'Helm': '☩',
               'Sloop': '☩',
               'Brig': '☩',
               'Galleon': '☩'
               }
      
cart = {}

item_count = sum([cart[key] for key in cart])

canv = Canvas(w)
f = Frame(canv)
scroll = Scrollbar(w,orient='vertical',command = canv.yview)
canv.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")
canv.pack(side="left", fill="both", expand=True)
canv.create_window((4,4), window=f, anchor="nw")

f.bind("<Configure>", lambda event, canvas=canv: onFrameConfigure(canvas))


welcomeMessage = Label(f,text='Welcome to the Pirate Shop!',font=pirateFont2)

welcome = LabelFrame(f, labelwidget=welcomeMessage)
welcome.grid(row=0,column=1)

cartMessage = Label(welcome, border=5, padding=3, relief=RAISED, background='gold', font=pirateFont1, foreground='crimson', text='Ahoy! Yer Carrrt is Empty!' if item_count == 0 else 'Ahoy! Yer Carrrt Has One Item' if item_count == 1 else f'Ahoy! Yer Carrrt Has {item_count} Items!')
cartMessage.pack()

menub = Menubutton(f,text='Menu')
menub.grid(row=1,column=1)

menub.menu = Menu(menub,tearoff=0,activeforeground='red')
menub['menu'] = menub.menu


viewCart = IntVar()
emptyCart = IntVar()
checkOut = IntVar()

menub.menu.add_checkbutton (label = f'View Carrrt ({item_count})', variable=viewCart)
menub.menu.add_checkbutton (label = 'Empty Carrrt', variable=emptyCart)
menub.menu.add_checkbutton (label = 'Checkout', variable=checkOut)



skull = PhotoImage(file='./piratestuff/btnskl.png')
btnskull = skull.subsample(15,15)





def addcart(item):
    global cart
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    global welcomeMessage
    global welcome
    welcomeMessage.destroy()
    welcome.destroy()
    welcomeMessage = Label(f,text='Welcome to the Pirate Shop!',font=pirateFont2)
    welcome = LabelFrame(f, labelwidget=welcomeMessage)
    welcome.grid(row=0,column=1)

    

        

class forSale:
    def __init__(self,name):
        self.name = name
        self.price = item_prices[name]
        self.row = ([key for key in item_prices].index(self.name) // 3) + 2
        self.col = [key for key in item_prices].index(self.name) % 3
    def place(self):
        fra = Frame(f)
        fra.grid(row = self.row, column = self.col)
        pic = PhotoImage(file=f"./piratestuff/{''.join((self.name).lower().split())}.png")
        lab = Label(fra,text=f"{self.name} for only {self.price}")
        lab['font'] = pirateFont8
        lab.pack()
        photo = Button(fra,height=320,width=320,image=pic)
        photo.pack()
        quantity = Spinbox(fra, from_ = 0, to_ = 1000)
        quantity.pack()
        butt = Button(fra,text = 'Add to Carrrt', bg='black', activebackground='yellow', cursor='pirate', fg='white', activeforeground='red', image=btnskull, compound = LEFT, command = lambda: addcart(self.name))
        butt['font'] = pirateFont7
        butt.pack()

for key in item_prices:
    item = forSale(key)
    item.place()


w.mainloop()

