import tkinter as tk
from tkinter import ttk

class WidgetsFactory:#-----------------------------------------widget factory----------------------------------------

    @staticmethod
    def create_button(parent, text, command=None, width=None, height=None, bg='forestgreen'):
        return tk.Button(parent, text=text, command=command, width=width, height=height, bg=bg)
    
    @staticmethod
    def create_label(parent, text, font=("Courier", 10), bg='forestgreen', fg='black'):
        label = tk.Label(parent, text=text, bg=bg, fg=fg)
        label.configure(font=font)
        return label
    
    @staticmethod
    def create_entry(parent, show='', width=40, bg='white'):
        return tk.Entry(parent, show=show, width=width, bg=bg)
    
    @staticmethod
    def create_text(parent):
        return tk.Text(parent)
    
    @staticmethod
    def create_combobox(parent, values=[], state='readonly'):
        return ttk.Combobox(parent, values=values, state=state)

    @staticmethod
    def create_separator(parent, orient):
        return ttk.Separator(parent, orient=orient)
    
    @staticmethod
    def create_frame(parent, width=None, height=None, bg='chartreuse', bd=None, relief=None):
        return tk.Frame(parent, width=width, height=height, bg=bg, bd=bd, relief=relief)
    
    @staticmethod
    def create_listbox(parent, width=None, height=None, bg='white', selectmode=None):
        return tk.Listbox(parent, width=width, height=height, bg=bg, selectmode=selectmode)

    @staticmethod
    def create_progressbar(parent, orient='horizontal', length=100, mode='determinate'):
        return ttk.Progressbar(parent, orient=orient, length=length, mode=mode)
    
    @staticmethod
    def create_image_label(parent, image_path):
        image = tk.PhotoImage(file=image_path)
        label = tk.Label(parent, image=image)
        label.image = image  
        return label
    
    @staticmethod
    def configure_widget(widget, bg=None, fg=None):
        if bg:
            widget.config(bg=bg)
        if fg:
            widget.config(fg=fg)
