import tkinter
from tkinter import filedialog, messagebox, ttk, colorchooser, font
import os

if __name__ == '__main__':

    font_format = ("ubuntu", 12)

    main_window = tkinter.Tk()
    main_window.geometry("1000x750+300+60")
    main_window.resizable(True, True)
    main_window.title(string="Text Editor By APD")
    main_window.iconbitmap('text_icon.ico')

    # ======== defining menu bar ============
    my_menu = tkinter.Menu(main_window, tearoff=False)
    main_window.config(menu=my_menu)

    #
    # ========== tool bar and status bar hide ==========
    show_status_bar = tkinter.BooleanVar()
    show_status_bar.set(True)
    show_tool_bar = tkinter.BooleanVar()
    show_tool_bar.set(True)

    # tool_bar = tkinter.ttk.Label(main_window)
    # tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)

    # status_bar = tkinter.Label(main_window, text="Status Bar", font='times 14 italic')
    # status_bar.pack(side=tkinter.BOTTOM)

    def hide_toolbar():
        global show_tool_bar
        if show_tool_bar:
            tool_bar.pack_forget()
            show_tool_bar = False
        else:
            text_box.pack_forget()
            status_bar.pack_forget()
            tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)
            text_box.pack(fill=tkinter.BOTH, expand=True)
            status_bar.pack(side=tkinter.BOTTOM)
            show_tool_bar = True

    def hide_statusbar():
        global show_status_bar
        if show_status_bar:
            status_bar.pack_forget()
            show_status_bar = False
        else:
            status_bar.pack(side=tkinter.BOTTOM)
            show_status_bar = True

    # =============================== defining menu functions =======================================================
    def new_page():
        warn = tkinter.messagebox.askquestion("Are you sure?", "Open new page without saving this one?", icon="warning")
        if warn == 'yes':
            text_box.delete(0.0, tkinter.END)
        else:
            pass

    def open_file():
        filename = filedialog.askopenfile(initialdir=os.getcwd(), title='Select a file', filetypes=(("text document", "*.txt"), ))
        try:
            text = filename.read()
            print(text)
            text_box.delete(0.0, tkinter.END)
            text_box.insert(tkinter.INSERT, text)
        except Exception:
            pass

    def save_file():
        details = text_box.get(0.0, tkinter.END)
        print(details)

        try:
            file_name = filedialog.asksaveasfilename(initialdir='D:/', title='Save Text File', filetypes=(("text document(.txt)", "*.txt"), ))
            file = open(file_name + ".txt", 'w', encoding='utf-8')
            file.write(details)
            file.close()
            tkinter.messagebox.showinfo("Success", "File saved", icon='info')
        except Exception:
            pass

    def cut_text():
        print("CUT TEXT")
        text_box.event_generate(("<<Cut>>"))

    def copy_text():
        print("COPY TEXT")
        text_box.event_generate(("<<Copy>>"))

    def paste_text():
        print("PASTE TEXT")
        text_box.event_generate(("<<Paste>>"))

    def about_app():
        tkinter.messagebox.showinfo("About App", "This is notepad by Amar Preet Das")

    def exit_app():
        tkinter.messagebox.showinfo("Exit", "Thanks for using my app")
        main_window.destroy()
    #
    #
    # ================== defining icons ===========================
    new_icon = tkinter.PhotoImage(file='images/new_page.png')
    open_icon = tkinter.PhotoImage(file='images/open.png')
    save_icon = tkinter.PhotoImage(file='images/save.png')
    exit_icon = tkinter.PhotoImage(file='images/exit.png')
    cut_icon = tkinter.PhotoImage(file='images/cut.png')
    copy_icon = tkinter.PhotoImage(file='images/copy.png')
    paste_icon = tkinter.PhotoImage(file='images/paste.png')
    info_icon = tkinter.PhotoImage(file='images/info.png')
    tool_icon = tkinter.PhotoImage(file='images/toolbar.png')

    # ======= creating menu lists ==============================================================================================================

    file_menu = tkinter.Menu(my_menu, font=font_format, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)           # File menu
    file_menu.add_command(label="New Page", image=new_icon, compound=tkinter.LEFT, accelerator="Ctrl+N", command=new_page)   # New page(, image=new_icon)
    file_menu.add_command(label="Open..", image=open_icon, compound=tkinter.LEFT, command=open_file)    # Open
    file_menu.add_command(label="Save As..", image=save_icon, compound=tkinter.LEFT, accelerator="Ctrl+S", command=save_file)       # Save as
    file_menu.add_separator()
    file_menu.add_command(label="Exit", image=exit_icon, compound=tkinter.LEFT, command=exit_app)    # Exit

    edit_menu = tkinter.Menu(my_menu, font=font_format, tearoff=0)
    my_menu.add_cascade(label='Edit', menu=edit_menu)           # Edit menu
    edit_menu.add_command(label='Cut', image=cut_icon, compound=tkinter.LEFT, accelerator="Ctrl+X", command=cut_text)    # Cut
    edit_menu.add_command(label='Copy', image=copy_icon, compound=tkinter.LEFT, accelerator="Ctrl+C", command=copy_text)   # copy
    edit_menu.add_command(label='Paste', image=paste_icon, compound=tkinter.LEFT, accelerator="Ctrl+V", command=paste_text)  # paste

    view_menu = tkinter.Menu(my_menu, font=font_format, tearoff=0)
    my_menu.add_cascade(label='View', menu=view_menu)           # View menu
    view_menu.add_checkbutton(label='Tool Bar', image=tool_icon, compound=tkinter.LEFT, variable=show_tool_bar, onval=True, offvalue=False, command=hide_toolbar)   # image=name
    view_menu.add_checkbutton(label='Status Bar', image=tool_icon, compound=tkinter.LEFT, variable=show_status_bar, onval=True, offvalue=False, command=hide_statusbar)   # image=name

    about_menu = tkinter.Menu(my_menu, font=font_format, tearoff=0)
    my_menu.add_cascade(label='About', menu=about_menu)         # About menu
    about_menu.add_command(label='Info', image=info_icon, compound=tkinter.LEFT, command=about_app)

    #
    # ====================================================================================================
    # ========== tool bar Label ============
    tool_bar = tkinter.ttk.Label(main_window)
    tool_bar.pack(side=tkinter.TOP, fill=tkinter.X)

    # ========= Font Box =================
    font_tuple = tkinter.font.families()
    font_family = tkinter.StringVar()
    font_box = tkinter.ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
    font_box["values"] = font_tuple
    font_box.current(font_tuple.index("Arial"))
    font_box.grid(row=0, column=0, padx=5, pady=5)

    # ======= Size box =================
    size_var = tkinter.IntVar()
    font_size = tkinter.ttk.Combobox(tool_bar, width=20, textvariable=size_var, state='readonly')
    font_size["values"] = tuple(range(2, 100, 2))
    font_size.current(5)
    font_size.grid(row=0, column=1, padx=5)

    # ======= Bold Button =================
    # text_label = tkinter.Label(main_window, text="")
    # text_label.pack()
    # def sele():
    #     selected = text_box.selection_get()
    #     text_label.config(text=selected)

    def bold_text():
        bold_text = tkinter.font.Font(text_box, text_box.cget("font"))
        bold_text.configure(weight='bold')

        text_box.tag_configure("bold", font=bold_text)

        current_tags = text_box.tag_names("sel.first")

        if "bold" in current_tags:
            text_box.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_box.tag_add("bold", "sel.first", "sel.last")

    bold_icon = tkinter.PhotoImage(file='images/bold_image.png')
    bold_button = tkinter.ttk.Button(tool_bar, image=bold_icon, command=bold_text)    # replace text with image=bold_icon
    bold_button.grid(row=0, column=2, padx=5)

    # ======= Italic Button =================

    def italic_text():
        italic_text = tkinter.font.Font(text_box, text_box.cget("font"))
        italic_text.configure(slant='italic')

        text_box.tag_configure("italic", font=italic_text)

        current_tags = text_box.tag_names("sel.first")

        if "italic" in current_tags:
            text_box.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_box.tag_add("italic", "sel.first", "sel.last")

    italic_icon = tkinter.PhotoImage(file='images/italic_image.png')
    italic_button = tkinter.ttk.Button(tool_bar, image=italic_icon, command=italic_text)    # replace text="" with image=bold_icon
    italic_button.grid(row=0, column=3, padx=5)

    # ======= Underline Button =================

    def underline_text():
        underline_text = tkinter.font.Font(text_box, text_box.cget("font"))
        underline_text.configure(underline=1)

        text_box.tag_configure("underline", font=underline_text)

        current_tags = text_box.tag_names("sel.first")

        if "underline" in current_tags:
            text_box.tag_remove("underline", "sel.first", "sel.last")
            print("if")
        else:
            text_box.tag_add("underline", "sel.first", "sel.last")
            print("else")

    underline_icon = tkinter.PhotoImage(file='images/underline_image.png')
    underline_button = tkinter.ttk.Button(tool_bar, image=underline_icon, command=underline_text)    # replace text with image=bold_icon
    underline_button.grid(row=0, column=4, padx=5)

    # ======= Font color Button =================
    fontcolor_icon = tkinter.PhotoImage(file='images/fontcolor_image.png')
    fontcolor_button = tkinter.ttk.Button(tool_bar, image=fontcolor_icon)    # replace text with image=bold_icon
    fontcolor_button.grid(row=0, column=5, padx=5)

    # ======= Left Align Button =================
    leftalign_icon = tkinter.PhotoImage(file='images/leftalign_iage.png')
    leftalign_button = tkinter.ttk.Button(tool_bar, image=leftalign_icon)    # replace text with image=bold_icon
    leftalign_button.grid(row=0, column=6, padx=5)

    # ======= Center Align Button =================
    center_icon = tkinter.PhotoImage(file='images/centeralign_image.png')
    center_button = tkinter.ttk.Button(tool_bar, image=center_icon)    # replace text with image=bold_icon
    center_button.grid(row=0, column=7, padx=5)

    # ======= Right Align Button =================
    rightalign_icon = tkinter.PhotoImage(file='images/rightalign_image.png')
    rightalign_button = tkinter.ttk.Button(tool_bar, image=rightalign_icon)    # replace text with image=bold_icon
    rightalign_button.grid(row=0, column=8, padx=5)

    # ====================================================================================================
    #
    # ========== Toolbar functions ===============
    font_type_now = "Arial"
    font_size_now = 12

    def change_font_type(main_window):
        global font_size_now, font_type_now
        font_type_now = font_family.get()
        text_box.configure(font=(font_type_now, font_size_now))

    def change_font_size(main_window):
        global font_size_now
        font_size_now = size_var.get()
        text_box.configure(font=(font_type_now, font_size_now))

    font_box.bind("<<ComboboxSelected>>", change_font_type)
    font_size.bind("<<ComboboxSelected>>", change_font_size)

    def color_choose():
        color_var = tkinter.colorchooser.askcolor()
        text_box.configure(fg=color_var[1])

    fontcolor_button.configure(command=color_choose)

    def align_left():
        text_get_all = text_box.get(1.0, "end")
        text_box.tag_config("left", justify=tkinter.LEFT)
        text_box.delete(1.0, tkinter.END)
        text_box.insert(tkinter.INSERT, text_get_all, "left")

    leftalign_button.configure(command=align_left)

    def align_center():
        text_get_all = text_box.get(1.0, "end")
        text_box.tag_config("center", justify=tkinter.CENTER)
        text_box.delete(1.0, tkinter.END)
        text_box.insert(tkinter.INSERT, text_get_all, "center")

    center_button.configure(command=align_center)

    def align_right():
        text_get_all = text_box.get(1.0, "end")
        text_box.tag_config("right", justify=tkinter.RIGHT)
        text_box.delete(1.0, tkinter.END)
        text_box.insert(tkinter.INSERT, text_get_all, "right")

    rightalign_button.configure(command=align_right)

    # ====================================================================================================
    #
    # ========== Text Box ===============
    text_box = tkinter.Text(main_window, font='{} {} {}'.format('lucida', "11", 'roman'), insertwidth=1, bg='white', fg='{}'.format('black'), border=1)
    text_box.config(wrap='word', relief=tkinter.FLAT)
    text_box.pack(expand=True, fill=tkinter.BOTH)
    text_box.focus_set()        # pre set ruler mouse on notepad

    print(tkinter.font.Font(font=text_box["font"]).actual())        # display all the current text formats

    # ========== Scroll Bar ============
    scroll_bar = tkinter.Scrollbar(text_box)
    scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    scroll_bar.config(command=text_box.yview)
    text_box.config(yscrollcommand=scroll_bar.set)

    # ====================================================================================================
    # ==========  Status Bar ============
    status_bar = tkinter.Label(main_window, text="Status Bar", font='times 14 italic')
    status_bar.pack(side=tkinter.BOTTOM)

    text_change = False

    def change_words(event=None):
        global text_change
        if text_box.edit_modified():
            text_change =True
            word = len(text_box.get(1.0, "end-1c").split())
            character = len(text_box.get(1.0, "end-1c").replace(" ", ""))
            status_bar.config(text=f"character: {character} word: {word}")
        text_box.edit_modified(False)

    text_box.bind("<<Modified>>", change_words)

    main_window.mainloop()
