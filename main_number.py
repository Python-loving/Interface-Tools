from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from code.number import numberchoix

def number():
    home = tk.Toplevel()
    home.title("WHITEWOLF-TOOLS")
    home.geometry("1200x560")
    home.minsize(1200, 560)
    home.iconbitmap("icon-tool.ico")
    home.configure(bg="black")
    home.grid_columnconfigure(0, weight=1)
    home.grid_columnconfigure(1, weight=1)
    home.grid_rowconfigure(0, weight=1)

    hautdroite_frame = Frame(home, bg="black")
    hautdroite_frame.grid(row=0, column=1, sticky="ne", padx=(0, 150))

    hautdroite2_frame = Frame(home, bg="black")
    hautdroite2_frame.grid(row=0, column=1, sticky="e", padx=(0, 50))

    bg_label = tk.Label(home, bg="black")
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
        nonlocal frame_index

        bg_label.config(image=frames[frame_index])

        frame_index = (frame_index + 1) % len(frames)

        home.after(1000, animate)

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

    NUMBER = Entry(hautdroite2_frame, font=("Orbitron", 14, "bold"), fg="white", bg="#1a1a1a", insertbackground="#00ffff", relief="flat", bd=0, width=20, justify="center")
    NUMBER.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipady=8)
    NUMBER.insert(0, "number...")

    def confirm():
        number_value = NUMBER.get()
        numberchoix(number_value, result_label)

    CONF = Button(hautdroite2_frame, text="CONFIRMER", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2", command=confirm)

    CONF.grid(row=1, column=0, pady=10, padx=10)

    def EXIT():
        subprocess.call("taskkill /F /IM python.exe", shell=True)

    EXIT = Button(hautdroite2_frame, text="EXIT", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2", command=EXIT)

    EXIT.grid(row=1, column=1, pady=10, padx=10)

    result_label = Label(hautdroite2_frame, text="", fg="white", bg="#111111", font=("Orbitron", 12))

    result_label.grid(row=2, column=0, columnspan=2)


    hautdroite_frame.lift()

    hautdroite2_frame.lift()

    home.mainloop()