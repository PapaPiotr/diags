import os
import sys
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk

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

root = tk.Tk()

def openSettings():
    settingsWindow = tk.Toplevel(root)
    settingsWindow.title("Settings")

    titleVal = 0
    titleBox = tk.Checkbutton(settingsWindow, text='Show title', variable=titleVal)
    titleBox.grid(column=0, row=0, sticky=tk.W)

    pageNumVal = 0
    pageNumBox = tk.Checkbutton(settingsWindow, text='Page numbering', variable=pageNumVal)
    pageNumBox.grid(column=0, row=1, sticky=tk.W)

    orientationLabel = tk.Label(settingsWindow, text='Page orientation')
    orientationLabel.grid(column=0, row=2, columnspan=3, sticky=tk.W)
    orientationOpts = tk.StringVar()
    orientationCombo = ttk.Combobox(settingsWindow, textvariable=orientationOpts)
    orientationCombo['values'] = ("Landscape","Portrait")
    orientationCombo.grid(column=5, row=2, columnspan=4, sticky=tk.EW)

    diagramNumLabel = tk.Label(settingsWindow, text="Number of diagrams")
    diagramNumLabel.grid(column=0, row=3, columnspan=4, sticky=tk.W)
    diagramNumVal = 1
    diagramNumSpin = tk.Spinbox(settingsWindow, from_=1, to=15, textvariable=diagramNumVal, wrap=False)
    diagramNumSpin.grid(column=5, row=3, sticky=tk.EW)

    rowNumLabel = tk.Label(settingsWindow, text="Number of rows")
    rowNumLabel.grid(column=0, row=4, columnspan=4, sticky=tk.W)
    rowNumVal = 1
    rowNumSpin = tk.Spinbox(settingsWindow, from_=1, to=15, textvariable=rowNumVal, wrap=False)
    rowNumSpin.grid(column=5, row=4, sticky=tk.EW)

    marginPxLabel = tk.Label(settingsWindow, text="Padding")
    marginPxLabel.grid(column=0, row=4, columnspan=4, sticky=tk.W)
    marginPxVal = 1
    marginPxSpin = tk.Spinbox(settingsWindow, from_=1, to=15, textvariable=rowNumVal, wrap=False)
    marginPxSpin.grid(column=5, row=4, sticky=tk.EW)
    marginPxLabel2 = tk.Label(settingsWindow, text=".px")
    marginPxLabel2.grid(column=6, row=4, sticky=tk.W)

menubar = tk.Menu(root)
root.config(menu=menubar)

numberOfDiags=12
i=0

#Menu
file_menu = tk.Menu(menubar, tearoff = False)
help_menu = tk.Menu(menubar, tearoff = False)

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
        underline = 1,
        command = openSettings
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

toolbar = tk.Frame(root, bd=1, height=30, relief=tk.RAISED)
toolbar.grid(column=0, row=0, columnspan=5, sticky=tk.NSEW)

newImg = PIL.Image.open(newPath)
newImg = newImg.resize((25,25))
newE = PIL.ImageTk.PhotoImage(newImg)
newButton = tk.Button(toolbar, image=newE, relief=tk.FLAT)
newButton.pack(side=tk.LEFT, padx=2, pady=2)

foldImg = PIL.Image.open(foldPath)
foldImg = foldImg.resize((25,25))
foldE = PIL.ImageTk.PhotoImage(foldImg)
foldButton = tk.Button(toolbar, image=foldE, relief=tk.FLAT)
foldButton.pack(side=tk.LEFT, padx=2, pady=2)

viewImg = PIL.Image.open(viewPath)
viewImg = viewImg.resize((25,25))
viewE = PIL.ImageTk.PhotoImage(viewImg)
viewButton = tk.Button(toolbar, image=viewE, relief=tk.FLAT)
viewButton.pack(side=tk.LEFT, padx=2, pady=2)

saveImg = PIL.Image.open(savePath)
saveImg = saveImg.resize((25,25))
saveE = PIL.ImageTk.PhotoImage(saveImg)
saveButton = tk.Button(toolbar, image=saveE, relief=tk.FLAT)
saveButton.pack(side=tk.LEFT, padx=2, pady=2)

saveAsImg = PIL.Image.open(saveAsPath)
saveAsImg = saveAsImg.resize((25,25))
saveAsE = PIL.ImageTk.PhotoImage(saveAsImg)
saveAsButton = tk.Button(toolbar, image=saveAsE, relief=tk.FLAT)
saveAsButton.pack(side=tk.LEFT, padx=2, pady=2)

viewImg = PIL.Image.open(viewPath)
viewImg = viewImg.resize((25,25))
viewE = PIL.ImageTk.PhotoImage(viewImg)
viewButton = tk.Button(toolbar, image=viewE, relief=tk.FLAT)
viewButton.pack(side=tk.LEFT, padx=2, pady=2)

imgImg = PIL.Image.open(imgPath)
imgImg = imgImg.resize((25,25))
imgE = PIL.ImageTk.PhotoImage(imgImg)
imgButton = tk.Button(toolbar, image=imgE, relief=tk.FLAT)
imgButton.pack(side=tk.LEFT, padx=2, pady=2)

imgsImg = PIL.Image.open(imgsPath)
imgsImg = imgsImg.resize((25,25))
imgsE = PIL.ImageTk.PhotoImage(imgsImg)
imgsButton = tk.Button(toolbar, image=imgsE, relief=tk.FLAT)
imgsButton.pack(side=tk.LEFT, padx=2, pady=2)

settingsImg = PIL.Image.open(settingsPath)
settingsImg = settingsImg.resize((25,25))
settingsE = PIL.ImageTk.PhotoImage(settingsImg)
settingsButton = tk.Button(toolbar, image=settingsE, relief=tk.FLAT, command=openSettings)
settingsButton.pack(side=tk.LEFT, padx=2, pady=2)

aboutImg = PIL.Image.open(aboutPath)
aboutImg = aboutImg.resize((25,25))
aboutE = PIL.ImageTk.PhotoImage(aboutImg)
aboutButton = tk.Button(toolbar, image=aboutE, relief=tk.FLAT)
aboutButton.pack(side=tk.LEFT, padx=2, pady=2)

#Formulaire
labelTitre = tk.Label(root, text="Titre :")
entryTitre = tk.Entry(root)
labelTitre.grid(column=0,row=2, sticky=tk.W)
entryTitre.grid(column=1,row=2, sticky=tk.NSEW, columnspan=5)

labelFEN = tk.Label(root, text="Saisir un FEN ou un identifiant de problème Lichess")
labelFEN.grid(column=1,row=3, sticky=tk.NSEW, columnspan=3)

entrysFig = list()
labelsFig = list()
buttonsFig = list()

while i<numberOfDiags:
    labelsFig.append(tk.Label(root, text="Fig."+str(i+1)))
    entrysFig.append(tk.Entry(root))
    buttonsFig.append(tk.Button(root, text="Éditeur graphique"))
    i+=1
i=0

while i<numberOfDiags:
    labelsFig[i].grid(column=0,row=4+i, sticky=tk.W)
    entrysFig[i].grid(column=1,row=4+i, sticky=tk.NSEW, columnspan=3)
    buttonsFig[i].grid(column=4,row=4+i, sticky=tk.W)
    i+=1
i=0

labelNumPage = tk.Label(root, text="Numéro de page")
spinNumPage = tk.Spinbox(root, from_=1, to=9999, wrap=False)
labelFirstNum = tk.Label(root, text="Numéro du premier diagramme")
spinFirstNum = tk.Spinbox(root, from_=1, to=9999, wrap=False)

labelNumPage.grid(column=0,row=6+numberOfDiags, sticky=tk.W, columnspan=2)
spinNumPage.grid(column=3,row=6+numberOfDiags, sticky=tk.NSEW, columnspan=2)
labelFirstNum.grid(column=0,row=7+numberOfDiags, sticky=tk.W, columnspan=2)
spinFirstNum.grid(column=3,row=7+numberOfDiags, sticky=tk.NSEW, columnspan=2)

#Refresh
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()
