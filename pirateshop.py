from tkinter import *
from tkinter.ttk import *
#Comment out the line below if not on MacOSX and change the names of the options 'bg' and 'fg' in the Button to 'background' and 'foreground'
from tkmacosx import Button
import tkinter.font as font

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

w = Tk()
w.title('Pirate Shop')
w.geometry('1250x600')

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


item_prices = {'Pegleg': '10.00',
               'Eyepatch': '5.00',
               'Hook': '25.00',
               'Parrot': '40.00',
               'Cutlass': '50.00',
               'Blunderbuss': '60.00',
               'Musket': '75.00',
               'Gunpowder': '5.00',
               'Cannonball': '10.00',
               'Cannon': '200.00',
               'Jolly Roger': '25.00',
               'Bottle of Rum': '5.00',
               'Barrel of Rum': '50.00',
               'Treasure Map': '100.00',
               'Treasure Chest': '200.00',
               'Tricorne': '15.00',
               'Spyglass': '20.00',
               'Accordion': '25.00',
               'Compass': '15.00',
               'Pipe': '10.00',
               'Tobacco': '5.00',
               'Long Johns': '20.00',
               'Jabot': '10.00',
               'Bandana': '5.00',
               'Plank': '15.00',
               'Anchor': '80.00',
               'Helm': '90.00',
               'Sloop': '500.00',
               'Brig': '1000.00',
               'Galleon': '10000.00'
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

def updatemessage():
    update = Toplevel()
    update.geometry('200x100')
    updateframe = Frame(update)
    updateframe.pack()
    updatelab = Label(updateframe,text='Yer Items Arrr Now Updated!')
    updatelab.pack()
    updateok = Button(updateframe,text='Aye-aye',command=lambda:update.destroy())
    updateok.pack()

def updatequantity(item,q):
    if q == 0:
        cart.__delitem__(item)
    else:
        cart[item] = q
    cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
    menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)
    updatemessage()

def checkout():
    receipt = Toplevel()
    receipt.title('Thank You for Visiting the Pirate Shop!')
    receipt.geometry('400x400')
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
            tallylab = Label(tallyframe,text=f'{self.number} x {self.name} at ☩{self.price} each, for a total of ☩ {self.number*float(self.price):.2f}')
            tallylab.pack()
    for key in cart:
        tallyitem = checkoutItem(key)
        tallyitem.tally()
    total = '%.2f'%(sum([float(item_prices[key]) * cart[key] for key in cart]))
    grandtotal = Label(rf,text=f'For a Grand Total of {total[:-3]} Doubloons and {total[-2:]} cents' if len(cart) else 'Your Carrrt is Empty!')
    grandtotal.pack()

def cartview():
    cartViewer = Toplevel()
    cartViewer.title('Yer Carrrt')
    cartViewer.geometry('300x300')
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

def emptymessage():
    emptiness = Toplevel()
    emptiness.title('Emptied!')
    emptiness.geometry('200x100')
    emptyframe = Frame(emptiness)
    emptyframe.pack()
    emptylab = Label(emptyframe, text = 'Yer Carrrt Has Been Emptied!')
    emptylab.pack()
    emptyok = Button(emptyframe,text='Aye-aye',command=lambda:emptiness.destroy())
    emptyok.pack()

def cartempty():
    warning = Toplevel()
    warning.title('Empty Carrrt?')
    warning.geometry('200x100')
    warningframe = Frame(warning)
    warningframe.pack()
    warninglab = Label(warningframe, text='Arrr Ye Sure, Ye Scalawag?')
    warninglab.pack()
    def reallyempty():
        global cart
        cart = {}
        cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
        menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)
        emptymessage()
        warning.destroy()
    yesbutton = Button(warningframe, text='Aye-aye', command = lambda: reallyempty())
    yesbutton.pack()
    nobutton = Button(warningframe, text='No', command = lambda:warning.destroy())
    nobutton.pack()

menub.menu.add_checkbutton (label = f'View Carrrt ({sum([cart[key] for key in cart])})', command=lambda:cartview())
menub.menu.add_command (label = 'Empty Carrrt', command=lambda:cartempty())
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
    admsg = Toplevel()
    admsg.geometry('300x100')
    admsg.title('Added!')
    addframe = Frame(admsg)
    addframe.pack()
    addlab = Label(addframe,text = f'{q} x {item} Added To Yer Carrrt!')
    addlab.pack()
    adbtn = Button(addframe,text = 'Aye-aye',command=lambda:admsg.destroy())
    adbtn.pack()



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

