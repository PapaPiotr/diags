import PIL.Image
import PIL.ImageTk
from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

numberOfDiags=12
i=0

#Menu
file_menu = Menu(menubar, tearoff = False)
help_menu = Menu(menubar, tearoff = False)

file_menu.add_command(
        label='New file',
        underline = 0
)

file_menu.add_command(
        label='Open form',
        underline = 0
)

file_menu.add_command(
        label='Open pgn',
        underline = 5
)

file_menu.add_command(
        label='Save form',
        underline = 5
)

file_menu.add_command(
        label='Save form as',
        underline = 10
)

file_menu.add_command(
        label='Preview page',
        underline = 3
)

file_menu.add_command(
        label='Save page',
        underline = 0
)

file_menu.add_command(
        label='Save diagrams',
        underline = 5
)

file_menu.add_command(
        label='Settings',
        underline = 1
)

file_menu.add_command(
        label='Exit',
        underline = 1,
        command=root.destroy
)

menubar.add_cascade(
    label='File',
    menu=file_menu,
    underline = 2

)

help_menu.add_command(
        label='Help',
        underline = 0
)

help_menu.add_command(
        label='About',
        underline = 0
)

menubar.add_cascade(
    label='Help',
    menu=help_menu,
    underline = 0


)

#Layout
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(4+numberOfDiags, weight=1)
root.grid_columnconfigure(1, weight=1)

toolbar = Frame(root, bd=1, height=30, relief=RAISED)
toolbar.grid(column=0, row=0, columnspan=5, sticky=NSEW)

imgNew = PIL.Image.open("resources/add-document.png")
imgNew = imgNew.resize((25,25))
eNew = PIL.ImageTk.PhotoImage(imgNew)
newButton = Button(toolbar, image=eNew, relief=FLAT)
newButton.pack(side=LEFT, padx=2, pady=2)

imgFold = PIL.Image.open("resources/folder-open.png")
imgFold = imgFold.resize((25,25))
eFold = PIL.ImageTk.PhotoImage(imgFold)
foldButton = Button(toolbar, image=eFold, relief=FLAT)
foldButton.pack(side=LEFT, padx=2, pady=2)

imgView = PIL.Image.open("resources/overview.png")
imgView = imgView.resize((25,25))
eView = PIL.ImageTk.PhotoImage(imgView)
viewButton = Button(toolbar, image=eView, relief=FLAT)
viewButton.pack(side=LEFT, padx=2, pady=2)

imgSave = PIL.Image.open("resources/disk.png")
imgSave = imgSave.resize((25,25))
eSave = PIL.ImageTk.PhotoImage(imgSave)
saveButton = Button(toolbar, image=eSave, relief=FLAT)
saveButton.pack(side=LEFT, padx=2, pady=2)

imgSaveAs = PIL.Image.open("resources/floppy-disk-pen.png")
imgSaveAs = imgSaveAs.resize((25,25))
eSaveAs = PIL.ImageTk.PhotoImage(imgSaveAs)
saveAsButton = Button(toolbar, image=eSaveAs, relief=FLAT)
saveAsButton.pack(side=LEFT, padx=2, pady=2)

imgBinoculars = PIL.Image.open("resources/binoculars.png")
imgBinoculars = imgBinoculars.resize((25,25))
eBinoculars = PIL.ImageTk.PhotoImage(imgBinoculars)
binocularsButton = Button(toolbar, image=eBinoculars, relief=FLAT)
binocularsButton.pack(side=LEFT, padx=2, pady=2)

imgPic = PIL.Image.open("resources/picture.png")
imgPic = imgPic.resize((25,25))
ePic = PIL.ImageTk.PhotoImage(imgPic)
picButton = Button(toolbar, image=ePic, relief=FLAT)
picButton.pack(side=LEFT, padx=2, pady=2)

imgImgs = PIL.Image.open("resources/images.png")
imgImgs = imgImgs.resize((25,25))
eImgs = PIL.ImageTk.PhotoImage(imgImgs)
imgsButton = Button(toolbar, image=eImgs, relief=FLAT)
imgsButton.pack(side=LEFT, padx=2, pady=2)

imgSettings = PIL.Image.open("resources/settings-sliders.png")
imgSettings = imgSettings.resize((25,25))
eSettings = PIL.ImageTk.PhotoImage(imgSettings)
settingsButton = Button(toolbar, image=eSettings, relief=FLAT)
settingsButton.pack(side=LEFT, padx=2, pady=2)

imgAbout = PIL.Image.open("resources/comment-info.png")
imgAbout = imgAbout.resize((25,25))
eAbout = PIL.ImageTk.PhotoImage(imgAbout)
aboutButton = Button(toolbar, image=eAbout, relief=FLAT)
aboutButton.pack(side=LEFT, padx=2, pady=2)

#Formulaire
labelTitre = Label(root, text="Titre :")
entryTitre = Entry(root)
labelTitre.grid(column=0,row=2, sticky=W)
entryTitre.grid(column=1,row=2, sticky=NSEW, columnspan=5)

labelFEN = Label(root, text="Saisir un FEN ou un identifiant de problème Lichess")
labelFEN.grid(column=1,row=3, sticky=NSEW, columnspan=3)

entrysFig = list()
labelsFig = list()
buttonsFig = list()

while i<numberOfDiags:
    labelsFig.append(Label(root, text="Fig."+str(i+1)))
    entrysFig.append(Entry(root))
    buttonsFig.append(Button(root, text="Éditeur graphique"))
    i+=1
i=0

while i<numberOfDiags:
    labelsFig[i].grid(column=0,row=4+i, sticky=W)
    entrysFig[i].grid(column=1,row=4+i, sticky=NSEW, columnspan=3)
    buttonsFig[i].grid(column=4,row=4+i, sticky=W)
    i+=1
i=0

labelNumPage = Label(root, text="Numéro de page")
spinNumPage = Spinbox(root, from_=1, to=9999, wrap=False)
labelFirstNum = Label(root, text="Numéro du premier diagramme")
spinFirstNum = Spinbox(root, from_=1, to=9999, wrap=False)

labelNumPage.grid(column=0,row=6+numberOfDiags, sticky=W, columnspan=2)
spinNumPage.grid(column=3,row=6+numberOfDiags, sticky=NSEW, columnspan=2)
labelFirstNum.grid(column=0,row=7+numberOfDiags, sticky=W, columnspan=2)
spinFirstNum.grid(column=3,row=7+numberOfDiags, sticky=NSEW, columnspan=2)

#Refresh
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()

