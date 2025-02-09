from tkinter import *


root = Tk()

numberOfDiags=12
i=0

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(4+numberOfDiags, weight=1)
root.grid_columnconfigure(1, weight=1)

labelTitre = Label(root, text="Titre :")
entryTitre = Entry(root)
labelTitre.grid(column=0,row=0, sticky=W)
entryTitre.grid(column=1,row=0, sticky=NSEW, columnspan=5)

labelFEN = Label(root, text="Saisir un FEN ou un identifiant de problème Lichess")
labelFEN.grid(column=1,row=2, sticky=NSEW, columnspan=3)

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
    labelsFig[i].grid(column=0,row=3+i, sticky=W)
    entrysFig[i].grid(column=1,row=3+i, sticky=NSEW, columnspan=3)
    buttonsFig[i].grid(column=4,row=3+i, sticky=W)
    i+=1
i=0

labelNumPage = Label(root, text="Numéro de page")
spinNumPage = Spinbox(root, from_=1, to=9999, wrap=False)
labelFirstNum = Label(root, text="Numéro du premier diagramme")
spinFirstNum = Spinbox(root, from_=1, to=9999, wrap=False)

labelNumPage.grid(column=0,row=5+numberOfDiags, sticky=W, columnspan=2)
spinNumPage.grid(column=3,row=5+numberOfDiags, sticky=NSEW, columnspan=2)
labelFirstNum.grid(column=0,row=6+numberOfDiags, sticky=W, columnspan=2)
spinFirstNum.grid(column=3,row=6+numberOfDiags, sticky=NSEW, columnspan=2)

root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()

