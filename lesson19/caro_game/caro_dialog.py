import tkinter as tk
from tkinter import ttk, colorchooser

class Dialog(tk.Toplevel):
    def __init__(self, parent, title, dx, dy, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._parent = parent
        self._ok = False
        self.title(title)
        self.geometry(f"+{parent.winfo_x() + dx}+{parent.winfo_y() + dy}")
        self.resizable(False, False)
        
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(sticky="WENS", padx=6, pady=4)
        (button_frame := ttk.Frame(self)).grid(row=1, sticky="WE", padx=6, pady=8)
        ttk.Button(button_frame, text="Cancel", command=self._on_cancel).pack(side="right")
        ttk.Button(button_frame, text="OK", command=self._on_ok).pack(side="right", padx=10)

        self.bind('<Return>', self._on_ok)
        self.bind('<Escape>', self._on_cancel)

    def _on_ok(self, event=None):
        self._ok = True
        self.destroy()

    def _on_cancel(self, event=None):
        self._ok = False
        self.destroy()
        
    def do_modal(self):
        self.focus_set()
        self.grab_set()
        self.transient(self._parent)
        self._parent.wait_window(self)

    def is_ok(self):
        return self._ok


class NewDialog(Dialog):
    
    MAN_VS_MAN, MAN_VS_APP, APP_VS_MAN = 0, 1, 2
    
    def __init__(self, parent, title, dx, dy, *args, **kwargs):
        super().__init__(parent, title, dx, dy, *args, **kwargs)
        self._initialize()

    def _initialize(self):
        ttk.Label(self.main_frame, text="Mode:").grid(row=0, sticky="W")
        ttk.Label(self.main_frame, text="1st player:").grid(row=1, sticky="W")
        ttk.Label(self.main_frame, text="1st name:").grid(row=2, sticky="W")
        ttk.Label(self.main_frame, text="2nd name:").grid(row=3, sticky="W")

        self._mode = tk.IntVar()
        self._is_O_first = tk.BooleanVar()
        self._is_O_first.trace("w", self._on_change_first_player)
        self._1st_name = tk.StringVar()
        self._2nd_name = tk.StringVar()

        (mode_frame := ttk.Frame(self.main_frame)).grid(row=0, column=1, sticky="W")
        ttk.Radiobutton(mode_frame, text="man vs man", variable=self._mode, value=NewDialog.MAN_VS_MAN).pack(side="left")
        ttk.Radiobutton(mode_frame, text="man vs app", variable=self._mode, value=NewDialog.MAN_VS_APP).pack(side="left", padx=4)
        ttk.Radiobutton(mode_frame, text="app vs man", variable=self._mode, value=NewDialog.APP_VS_MAN).pack(side="left", padx=4)

        (firstplayer_frame := ttk.Frame(self.main_frame)).grid(row=1, column=1, sticky="W")
        ttk.Radiobutton(firstplayer_frame, text="X", variable=self._is_O_first, value=False).pack(side="left")
        ttk.Radiobutton(firstplayer_frame, text="O", variable=self._is_O_first, value=True).pack(side="left", padx=4)
        
        ttk.Entry(self.main_frame, textvariable=self._1st_name).grid(row=2, column=1, sticky="WE")
        ttk.Entry(self.main_frame, textvariable=self._2nd_name).grid(row=3, column=1, sticky="WE")

        for child in self.main_frame.winfo_children():
            child.grid(pady=2)

        self._is_O_first.set(False)
    
    def _on_change_first_player(self, *args):
        if self._1st_name.get() in ["", "O", "o", "X", "x"]:
            self._1st_name.set("O" if self._is_O_first.get() else "X")
        if self._2nd_name.get() in ["", "O", "o", "X", "x"]:
            self._2nd_name.set("X" if self._is_O_first.get() else "O")
    
    def get_mode(self):
        return self._mode.get()

    def is_O_first(self):
        return self._is_O_first.get()

    def get_1st_name(self):
        if name1 := self._1st_name.get():
            return name1
        return "O" if self._is_O_first.get() else "X"

    def get_2nd_name(self):
        if name2 := self._2nd_name.get():
            return name2
        return "X" if self._is_O_first.get() else "O"


class SettingsDialog(Dialog):
    # color_dic: {key: {"name": , "color": }}
    def __init__(self, parent, title, dx, dy, color_dict, *args, **kwargs):
        super().__init__(parent, title, dx, dy, *args, **kwargs)
        self._color_dict = color_dict
        self._initialize()

    def _initialize(self):
        self._buttons = {}
        for index, key in enumerate(self._color_dict):
            ttk.Label(self.main_frame, text=f"{self._color_dict[key]['name']} color:").grid(row=index, sticky="W")
            self._buttons[key] = tk.Button(self.main_frame, width=10, borderwidth=1, bg=self._color_dict[key]["color"],
                  command=self._on_change_color(key))
            self._buttons[key].grid(row=index, column=1, sticky="W")

        for child in self.main_frame.winfo_children():
            child.grid(pady=2)

    def _on_change_color(self, key):
        def _chage_color():
            if choosen_color := colorchooser.askcolor(parent=self, title=f"Choose the {self._color_dict[key]['name']} color",
                                  initialcolor=self._color_dict[key]['color'])[1]:
                self._buttons[key].configure(bg=choosen_color)
                self._color_dict[key]["color"] = choosen_color
            
        return _chage_color
    
    def get_color_dict(self):
        return self._color_dict
