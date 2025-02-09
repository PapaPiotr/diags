import os
import sys
import PIL.Image
import PIL.ImageTk
from tkinter import *

# Déterminer le chemin correct pour les ressources
if getattr(sys, 'frozen', False):
    # Si le script est exécuté depuis un binaire
    application_path = sys._MEIPASS  # Répertoire temporaire contenant les ressources
else:
    # Si en mode développement
    application_path = os.path.dirname(__file__)
aboutPath = os.path.join(application_path, 'resources', 'about.png')
foldPath = os.path.join(application_path, 'resources', 'fold.png')
imgPath = os.path.join(application_path, 'resources', 'img.png')
imgsPath = os.path.join(application_path, 'resources', 'imgs.png')
newPath = os.path.join(application_path, 'resources', 'new.png')
saveAsPath = os.path.join(application_path, 'resources', 'saveAs.png')
savePath = os.path.join(application_path, 'resources', 'save.png')
settingsPath = os.path.join(application_path, 'resources', 'settings.png')
aboutPath = os.path.join(application_path, 'resources', 'about.png')
viewPath = os.path.join(application_path, 'resources', 'view.png')

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

newImg = PIL.Image.open(newPath)
newImg = newImg.resize((25,25))
newE = PIL.ImageTk.PhotoImage(newImg)
newButton = Button(toolbar, image=newE, relief=FLAT)
newButton.pack(side=LEFT, padx=2, pady=2)

foldImg = PIL.Image.open(foldPath)
foldImg = foldImg.resize((25,25))
foldE = PIL.ImageTk.PhotoImage(foldImg)
foldButton = Button(toolbar, image=foldE, relief=FLAT)
foldButton.pack(side=LEFT, padx=2, pady=2)

viewImg = PIL.Image.open(viewPath)
viewImg = viewImg.resize((25,25))
viewE = PIL.ImageTk.PhotoImage(viewImg)
viewButton = Button(toolbar, image=viewE, relief=FLAT)
viewButton.pack(side=LEFT, padx=2, pady=2)

saveImg = PIL.Image.open(savePath)
saveImg = saveImg.resize((25,25))
saveE = PIL.ImageTk.PhotoImage(saveImg)
saveButton = Button(toolbar, image=saveE, relief=FLAT)
saveButton.pack(side=LEFT, padx=2, pady=2)

saveAsImg = PIL.Image.open(saveAsPath)
saveAsImg = saveAsImg.resize((25,25))
saveAsE = PIL.ImageTk.PhotoImage(saveAsImg)
saveAsButton = Button(toolbar, image=saveAsE, relief=FLAT)
saveAsButton.pack(side=LEFT, padx=2, pady=2)

viewImg = PIL.Image.open(viewPath)
viewImg = viewImg.resize((25,25))
viewE = PIL.ImageTk.PhotoImage(viewImg)
viewButton = Button(toolbar, image=viewE, relief=FLAT)
viewButton.pack(side=LEFT, padx=2, pady=2)

imgImg = PIL.Image.open(imgPath)
imgImg = imgImg.resize((25,25))
imgE = PIL.ImageTk.PhotoImage(imgImg)
imgButton = Button(toolbar, image=imgE, relief=FLAT)
imgButton.pack(side=LEFT, padx=2, pady=2)

imgsImg = PIL.Image.open(imgsPath)
imgsImg = imgsImg.resize((25,25))
imgsE = PIL.ImageTk.PhotoImage(imgsImg)
imgsButton = Button(toolbar, image=imgsE, relief=FLAT)
imgsButton.pack(side=LEFT, padx=2, pady=2)

settingsImg = PIL.Image.open(settingsPath)
settingsImg = settingsImg.resize((25,25))
settingsE = PIL.ImageTk.PhotoImage(settingsImg)
settingsButton = Button(toolbar, image=settingsE, relief=FLAT)
settingsButton.pack(side=LEFT, padx=2, pady=2)

aboutImg = PIL.Image.open(aboutPath)
aboutImg = aboutImg.resize((25,25))
aboutE = PIL.ImageTk.PhotoImage(aboutImg)
aboutButton = Button(toolbar, image=aboutE, relief=FLAT)
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

