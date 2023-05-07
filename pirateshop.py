from tkinter import *
from tkinter.ttk import *
#Comment out the line below if not on MacOSX and change the names of the options 'bg' and 'fg' in the Button to 'background' and 'foreground'
from tkmacosx import Button
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


item_prices = {'Pegleg': '',
               'Eyepatch': '',
               'Hook': '',
               'Parrot': '',
               'Cutlass': '',
               'Blunderbuss': '',
               'Musket': '',
               'Gunpowder': '',
               'Cannonball': '',
               'Cannon': '',
               'Jolly Roger': '',
               'Bottle of Rum': '',
               'Barrel of Rum': '',
               'Treasure Map': '',
               'Treasure Chest': '',
               'Tricorne': '',
               'Spyglass': '',
               'Accordion': '',
               'Compass': '',
               'Pipe': '',
               'Tobacco': '',
               'Long Johns': '',
               'Jabot': '',
               'Bandana': '',
               'Plank': '',
               'Anchor': '',
               'Helm': '',
               'Sloop': '',
               'Brig': '',
               'Galleon': ''
               }
      
cart = {}

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

cartMessage = Label(welcome, border=5, padding=3, relief=RAISED, background='gold', font=pirateFont1, foreground='crimson', text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
cartMessage.pack()

menub = Menubutton(f,text='Menu')
menub.grid(row=1,column=1)

menub.menu = Menu(menub,tearoff=0,activeforeground='red')
menub['menu'] = menub.menu

viewCart = IntVar()
emptyCart = IntVar()
checkOut = IntVar()

def updatequantity(item,q):
    if q == 0:
        cart.__delitem__(item)
    else:
        cart[item] = q
    cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
    menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)

def checkout():
    receipt = Toplevel()
    receipt.title('Thank You for Visiting the Pirate Shop!')
    rf = Frame(receipt)
    rf.pack()
    class checkoutItem:
        def __init__(self,name):
            self.name = name
            self.price = item_prices[name]
            self.number = cart[name]
        def tally(self):
            tallyframe = Frame(rf)
            tallyframe.pack()
            tallylab = Label(tallyframe,text=f'{self.number} x {self.name} for ☩{self.price} each, for a total of ☩')
            tallylab.pack()
    for key in cart:
        tallyitem = checkoutItem(key)
        tallyitem.tally()

def cartview():
    cartViewer = Toplevel()
    cartViewer.title('Yer Carrrt')
    cartframe = Frame(cartViewer)
    cartframe.pack()
    class cartItem:
        def __init__(self,name):
            self.name = name
        def listItem(self):
            itemframe = Frame(cartframe)
            itemframe.pack()
            itemlabel = Label(itemframe,text=self.name)
            itemlabel.pack(side=LEFT)
            quantity = Spinbox(itemframe, from_ = 0, to_ = 99999)
            quantity.insert(0,cart[self.name])
            update = Button(itemframe,text='Update Quantity',command=lambda:updatequantity(self.name,int(quantity.get())))
            update.pack(side=RIGHT)
            quantity.pack(side=RIGHT)
    for key in cart:
        cartitem = cartItem(key)
        cartitem.listItem()
    readycheck = Frame(cartframe)
    readycheck.pack()
    readymsg = Label(readycheck, text='Arrr You Ready to Check Out?')
    readymsg.pack(side=LEFT)
    checkoutnow = Button(readycheck, text='Check Out', command=lambda:checkout())
    checkoutnow.pack(side=RIGHT)
    continueshopping = Frame(cartframe)
    continueshopping.pack()
    continuelab = Label(continueshopping, text ='Or Do You Want To...')
    continuelab.pack(side=LEFT)
    continuebtn = Button(continueshopping, text = 'Keep Shopping!', command = lambda:cartViewer.destroy())
    continuebtn.pack()

        

def cartempty():
    pass

menub.menu.add_checkbutton (label = f'View Carrrt ({sum([cart[key] for key in cart])})', command=lambda:cartview())
menub.menu.add_command (label = 'Empty Carrrt')
menub.menu.add_command (label = 'Checkout', command=lambda:checkout())

skull = PhotoImage(file='./piratestuff/btnskl.png')
btnskull = skull.subsample(15,15)

def addcart(item,q):
    if item in cart:
        cart[item] += q
    else:
        cart[item] = q
    cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
    menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)

class forSale:
    def __init__(self,name):
        self.name = name
        self.price = item_prices[name]
        self.row = ([key for key in item_prices].index(self.name) // 3) + 2
        self.col = [key for key in item_prices].index(self.name) % 3
    def place(self):
        fra = Frame(f, borderwidth=5, padding=10, relief=RIDGE)
        fra.grid(row = self.row, column = self.col,pady=10)
        pic = PhotoImage(file=f"./piratestuff/{''.join((self.name).lower().split())}.png")
        lab = Label(fra,text=f"{self.name} for only ☩{self.price}",relief=GROOVE,foreground='light goldenrod')
        lab['font'] = pirateFont8
        lab.pack()
        photo = Button(fra,height=320,width=320,image=pic)
        photo.pack()
        quantity = Spinbox(fra, from_ = 0, to_ = 99999)
        quantity.insert(0,0)
        quantity.pack()
        butt = Button(fra,text = 'Add to Carrrt', bg='black', activebackground='yellow', cursor='pirate', fg='white', activeforeground='red', image=btnskull, compound = LEFT, command = lambda: addcart(self.name, int(quantity.get())))
        butt['font'] = pirateFont7
        butt.pack()

for key in item_prices:
    item = forSale(key)
    item.place()


w.mainloop()

