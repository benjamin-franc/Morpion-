from tkinter import *
from tkinter import messagebox


window= Tk()
window.title ("Morpion")

# si x commence, ca donne true 
clicked=True
count=0

# fonction pour desactiver tout les boutons 
def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#fonction pour verifier si un joueur a gagné.
def checkifwon():
    global winner
    winner=False
    if b1 ["text"]=="X" and b2 ["text"]=="X" and b3 ["text"]=="X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True 
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b4 ["text"]=="X" and b5 ["text"]=="X" and b6 ["text"]=="X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b7 ["text"]=="X" and b8 ["text"]=="X" and b9 ["text"]=="X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b1 ["text"]=="X" and b4 ["text"]=="X" and b7 ["text"]=="X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b2 ["text"]=="X" and b5 ["text"]=="X" and b8 ["text"]=="X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b3 ["text"]=="X" and b6 ["text"]=="X" and b9 ["text"]=="X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b1 ["text"]=="X" and b5 ["text"]=="X" and b9 ["text"]=="X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicition, le joueur X a gagné")
        disable_buttons()
    elif b3 ["text"]=="X" and b5 ["text"]=="X" and b7 ["text"]=="X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur X a gagné")
        disable_buttons()
    elif b1 ["text"]=="O" and b2 ["text"]=="O" and b3 ["text"]=="O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b4 ["text"]=="O" and b5 ["text"]=="O" and b6 ["text"]=="O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b7 ["text"]=="O" and b8 ["text"]=="O" and b9 ["text"]=="O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b1 ["text"]=="O" and b4 ["text"]=="O" and b7 ["text"]=="O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b2 ["text"]=="O" and b5 ["text"]=="O" and b8 ["text"]=="O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b3 ["text"]=="O" and b6 ["text"]=="O" and b9 ["text"]=="O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()
    elif b1 ["text"]=="O" and b5 ["text"]=="O" and b7 ["text"]=="O":
        b1.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Féliciation, le joueur O a gagné")
        disable_buttons()
    elif b3 ["text"]=="O" and b5 ["text"]=="O" and b7 ["text"]=="O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("Morpion","Félicitation, le joueur O a gagné")
        disable_buttons()

# verifie si egalité 

    if count==9 and winner==False:
        messagebox.showinfo("Morpion","Egalité !!")

# fonction du click des boutons

def b_click(b):
    global clicked, count
    if b ["text"]==" " and clicked==True:
        b ["text"]="X"
        clicked=False
        count +=1
        checkifwon()
    elif b ["text"]==" " and clicked==False:
        b ["text"]="O"
        clicked=True
        count +=1
        checkifwon()
    else:
        messagebox.showerror("Morpion","Hey ! ce carreau est déjà utilisé \n Choisit un autre...")

# creer les boutons (9 boutlons)

b1=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b1))
b2=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b2))
b3=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b3))

b4=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b4))
b5=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b5))
b6=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b6))

b7=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b7))
b8=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b8))
b9=Button(window, text=" ", font=("Helvetica" ,30), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b9))

# creer une grille pour les boutons

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# affiche notre fenetre

window.mainloop()