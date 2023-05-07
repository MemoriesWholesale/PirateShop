from tkinter import *
from tkinter.ttk import *
#Comment out the line below if not on MacOSX and change the names of the options 'bg' and 'fg' in the Button to 'background' and 'foreground'
from tkmacosx import Button
import tkinter.font as font

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

w = Tk()
w.title('Pirate Shop')
w.geometry('1400x600')

pirateFont1 = font.Font(family ='Trattatello', size=30)
pirateFont2 = font.Font(family ='Lucida Blackletter', size=45)
pirateFont3 = font.Font(family ='Apple Chancery', size=20)
pirateFont4 = font.Font(family ='Baskerville Old Face', size=14)
pirateFont5 = font.Font(family ='Cooper Black', size=20)
pirateFont6 = font.Font(family ='Edwardian Script ITC', size=20)
pirateFont7 = font.Font(family ='Goudy Old Style', size=20)
pirateFont8 = font.Font(family ='Kokonor', size=14)
pirateFont9 = font.Font(family ='Monotype Corsiva', size=20)
pirateFont10 = font.Font(family ='Zapfino', size=20)
pirateFont11 = font.Font(family ='Snell Roundhand', size=20)
pirateFont12 = font.Font(family ='Savoye LET', size=30)


item_prices = {'Pegleg': '11.95',
               'Eyepatch': '4.99',
               'Hook': '27.49',
               'Parrot': '42.01',
               'Cutlass': '49.99',
               'Blunderbuss': '54.95',
               'Musket': '79.99',
               'Gunpowder': '1.99',
               'Cannonball': '12.05',
               'Cannon': '199.95',
               'Jolly Roger': '26.49',
               'Bottle of Rum': '5.99',
               'Barrel of Rum': '59.99',
               'Treasure Map': '105.95',
               'Treasure Chest': '195.99',
               'Compass': '12.49',
               'Spyglass': '19.99',
               'Accordion': '26.49',
               'Pipe': '14.99',
               'Tobacco': '1.05',
               'Long Johns': '12.95',
               'Tricorne': '22.99',
               'Jabot': '9.99',
               'Bandana': '4.49',
               'Plank': '16.95',
               'Anchor': '78.95',
               'Helm': '88.99',
               'Sloop': '505.45',
               'Brig': '995.95',
               'Galleon': '9999.99'
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

welcomeMessage = Label(f,text='Welcome to the Pirate Shop!',font=pirateFont2,padding=10)

welcome = LabelFrame(f, labelwidget=welcomeMessage)
welcome.grid(row=0,column=1)

cartMessage = Label(welcome, border=5, padding=3, relief=RAISED, background='gold', font=pirateFont1, foreground='crimson', text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
cartMessage.pack()

menub = Menubutton(f,text='Menu')
menub.grid(row=1,column=1)

menub.menu = Menu(menub,tearoff=0,activeforeground='red',font=pirateFont8)
menub['menu'] = menub.menu

viewCart = IntVar()
emptyCart = IntVar()
checkOut = IntVar()

def updatemessage():
    update = Toplevel()
    update.geometry('200x100')
    updateframe = Frame(update)
    updateframe.pack()
    updatelab = Label(updateframe,text='Yer Items Arrr Now Updated!',font=pirateFont4)
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
    receipt.geometry('800x400')
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
            tallylab = Label(tallyframe,text=f'{self.number} x {self.name} at ☩{self.price} each, for a total of ☩{self.number*float(self.price):.2f}',font=pirateFont12)
            tallylab.pack()
    for key in cart:
        tallyitem = checkoutItem(key)
        tallyitem.tally()
    total = '%.2f'%(sum([float(item_prices[key]) * cart[key] for key in cart]))
    grandtotal = Label(rf,text=f'For a Grand Total of {total[:-3]} Doubloons and {total[-2:]} cents' if len(cart) else 'Yer Carrrt is Empty!',font=pirateFont10)
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
            itemlabel = Label(itemframe,text=self.name,font=pirateFont9)
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
    readymsg = Label(readycheck, text='Arrr Ye Ready to Check Out?',font=pirateFont4)
    readymsg.pack(side=LEFT)
    checkoutnow = Button(readycheck, text='Check Out', command=lambda:checkout())
    checkoutnow.pack(side=RIGHT)
    continueshopping = Frame(cartframe)
    continueshopping.pack()
    continuelab = Label(continueshopping, text ='Or Do Ye Want To...',font=pirateFont4)
    continuelab.pack(side=LEFT)
    continuebtn = Button(continueshopping, text = 'Keep Shopping!', command = lambda:cartViewer.destroy())
    continuebtn.pack()

def emptymessage():
    emptiness = Toplevel()
    emptiness.title('Emptied!')
    emptiness.geometry('200x100')
    emptyframe = Frame(emptiness)
    emptyframe.pack()
    emptylab = Label(emptyframe, text = 'Yer Carrrt Has Been Emptied!', font=pirateFont4)
    emptylab.pack()
    emptyok = Button(emptyframe,text='Aye-aye',command=lambda:emptiness.destroy())
    emptyok.pack()

def cartempty():
    warning = Toplevel()
    warning.title('Empty Carrrt?')
    warning.geometry('200x100')
    warningframe = Frame(warning)
    warningframe.pack()
    warninglab = Label(warningframe, text='Arrr Ye Sure, Ye Scalawag??',font=pirateFont4)
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


"""def addcart(item,q):
    if item in cart:
        cart[item] += q
    elif q > 0:
        cart[item] = q
    cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
    menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)
    admsg = Toplevel()
    admsg.geometry('300x100')
    admsg.title('Added!')
    addframe = Frame(admsg)
    addframe.pack()
    addlab = Label(addframe,text = f'{q} x {item} Added To Yer Carrrt!',font=pirateFont4)
    addlab.pack()
    adbtn = Button(addframe,text = 'Aye-aye',command=lambda:admsg.destroy())
    adbtn.pack()"""



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
        lab = Label(fra,text=f"{self.name} for just... \t ☩{self.price} !!",relief=GROOVE,foreground='light goldenrod',font=pirateFont3)
        lab.pack()
        photo = Button(fra,height=320,width=320,image=pic)
        photo.pack()
        quantity = Spinbox(fra, from_ = 0, to_ = 99999)
        quantity.insert(0,0)
        quantity.pack()
        def addcart(item,q):
            if item in cart:
                cart[item] += q
            elif q > 0:
                cart[item] = q
            cartMessage.config(text='Ahoy! Yer Carrrt is Empty!' if sum([cart[key] for key in cart]) == 0 else 'Ahoy! Yer Carrrt Has One Item!' if sum([cart[key] for key in cart]) == 1 else f'Ahoy! Yer Carrrt Has {sum([cart[key] for key in cart])} Items!')
            menub.menu.entryconfigure(0,label = f'View Carrrt ({sum([cart[key] for key in cart])})', variable=emptyCart)
            admsg = Toplevel()
            admsg.geometry('300x100')
            admsg.title('Added!')
            addframe = Frame(admsg)
            addframe.pack()
            addlab = Label(addframe,text = f'{q} x {item} Added To Yer Carrrt!',font=pirateFont4)
            addlab.pack()
            adbtn = Button(addframe,text = 'Aye-aye',command=lambda:admsg.destroy())
            adbtn.pack()
            quantity.delete(0,len(quantity.get()))
            quantity.insert(0,0)
        butt = Button(fra,text = 'Add to Carrrt', bg='black', activebackground='yellow', cursor='pirate', fg='white', activeforeground='red', image=btnskull, compound = LEFT, command = lambda: addcart(self.name, int(quantity.get())))
        butt['font'] = pirateFont7
        butt.pack()

for key in item_prices:
    item = forSale(key)
    item.place()


w.mainloop()

