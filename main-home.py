from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

window = tk.Tk()
window.title("WHITEWOLF-TOOLS")
window.geometry("1200x560")
window.minsize(1200, 560)
window.iconbitmap("icon-tool.ico")
window.configure(bg="black")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

hautdroite_frame = Frame(window, bg="black")
hautdroite_frame.grid(row=0, column=1, sticky="ne", padx=(0, 150))

hautdroite2_frame = Frame(window, bg="black")
hautdroite2_frame.grid(row=0, column=1, sticky="e", padx=(0, 50))

bg_label = tk.Label(window, bg="black")
bg_label.place(x=0, rely=0.5, anchor="w")

gif = Image.open("back.gif")
frames = []

try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(len(frames))
except Exception as e:
    print(f"ERROR {e}")
    pass

frame_index = 0

def animate():
    global frame_index

    bg_label.config(image=frames[frame_index])

    frame_index = (frame_index + 1) % len(frames)

    window.after(1, animate)

animate()

texte_complet = f"""
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗  
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝  
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║     
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝    """

titre = tk.Label(hautdroite_frame, text=texte_complet, bg="black", fg="white", font=("Courier New", 7, "bold"))

titre.pack()

LOOKUP = Button(hautdroite2_frame, text="LOOKUP", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

LOOKUP.grid(row=0, column=0, padx=10)

SECU = Button(hautdroite2_frame, text="Sécurity", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

SECU.grid(row=0, column=1, padx=10)

DISCORD = Button(hautdroite2_frame, text="Discord", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

DISCORD.grid(row=0, column=2, padx=10)

COVID = Button(hautdroite2_frame, text="Covid", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

COVID.grid(row=0, column=3, padx=10)

EXIT = Button(hautdroite2_frame, text="EXIT", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

EXIT.grid(row=0, column=3, padx=10)


hautdroite_frame.lift()

hautdroite2_frame.lift()

window.mainloop()