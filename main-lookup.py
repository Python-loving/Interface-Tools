def lookup():
    lookup = tk.Toplevel()
    lookup.title("WHITEWOLF-TOOLS")
    lookup.geometry("1200x560")
    lookup.minsize(1200, 560)
    lookup.iconbitmap("icon-tool.ico")
    lookup.configure(bg="black")
    lookup.grid_columnconfigure(0, weight=1)
    lookup.grid_columnconfigure(1, weight=1)
    lookup.grid_rowconfigure(0, weight=1)

    hautdroite_frame = Frame(lookup, bg="black")
    hautdroite_frame.grid(row=0, column=1, sticky="ne", padx=(0, 150))

    hautdroite2_frame = Frame(lookup, bg="black")
    hautdroite2_frame.grid(row=0, column=1, sticky="e", padx=(0, 50))

    hautdroite3_frame = Frame(lookup, bg="black")
    hautdroite3_frame.grid(row=1, column=1, pady=20)

    bg_label = tk.Label(lookup, bg="black")
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

        lookup.after(1, animate)

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

    IP = Button(hautdroite2_frame, text="IP", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

    IP.grid(row=0, column=0, padx=10)

    NUMBER = Button(hautdroite2_frame, text="Number", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

    NUMBER.grid(row=0, column=1, padx=10)

    USER = Button(hautdroite2_frame, text="Username", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

    USER.grid(row=0, column=2, padx=10)

    GOOGLE = Button(hautdroite2_frame, text="Google", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

    GOOGLE.grid(row=0, column=3, padx=10)

    DNS = Button(hautdroite2_frame, text="Dns", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2")

    DNS.grid(row=0, column=4, padx=10)

    def EXIT():
        subprocess.call("taskkill /F /IM python.exe", shell=True)

    EXIT = Button(hautdroite3_frame, text="EXIT", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2", command=EXIT)

    EXIT.grid(row=0, column=0, padx=10)


    hautdroite_frame.lift()

    hautdroite2_frame.lift()

    lookup.mainloop()