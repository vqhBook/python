import string, json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import caro_dialog

class Settings:
    def __init__(self):
        # https://www.rapidtables.com/web/color/gray-color.html
        self.back_color = "#FFC0CB"         # Pink
        self.grid_color = "#A9A9A9"         # Dark Gray
        self.highlight_color = "#FFFF00"    # Yellow
        self.X_color = "#FF0000"           # Red
        self.O_color = "#0000FF"            # Blue

        self.title = "Caro Game"
        self.cell_width = 25 # pixels 25
        self.width, self.height = 20, 20 # cells 20, 20
        self.padx, self.pady = 0, 0 # pixel each margin 5, 5
        self.X_char, self.O_char = "X", "O"
        self.XO_font = ("Arial bold", self.cell_width - 6)
        
        # https://www.iconfinder.com/iconsets/32x32-free-design-icons
        self.app_icon = tk.PhotoImage(file="caro_icon.png")
        self.new_icon = tk.PhotoImage(file="new_icon.png")
        self.open_icon = tk.PhotoImage(file="open_icon.png")
        self.save_icon = tk.PhotoImage(file="save_icon.png")
        self.undo_icon = tk.PhotoImage(file="undo_icon.png")
        self.redo_icon = tk.PhotoImage(file="redo_icon.png")
        self.settings_icon = tk.PhotoImage(file="settings_icon.png")

class CaroGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cur_cell_id = None
        self._moves_id = []
        self._cell_line_id = []
        self.sett = Settings()
        self.title(self.sett.title)
        self.resizable(False, False)
        self.iconphoto(True, self.sett.app_icon)

        self._initialize()
        self._start("Press New to play new game or Open to open an existing game")

    def _initialize(self):
        (toolbar_frame := ttk.Frame(self, relief="raised")).grid(ipady=2, sticky="EW")
        ttk.Button(toolbar_frame, image=self.sett.new_icon, command=self._on_new).pack(side="left")
        ttk.Button(toolbar_frame, image=self.sett.open_icon, command=self._on_open).pack(side="left")
        self._save_button = ttk.Button(toolbar_frame, image=self.sett.save_icon, command=self._on_save)
        self._save_button.pack(side="left")
        ttk.Button(toolbar_frame, image=self.sett.settings_icon, command=self._on_settings).pack(side="left", padx=10)
        self._undo_button = ttk.Button(toolbar_frame, image=self.sett.undo_icon, command=self._on_undo)
        self._undo_button.pack(side="left")
        self._redo_button = ttk.Button(toolbar_frame, image=self.sett.redo_icon, command=self._on_redo)
        self._redo_button.pack(side="left")
        
        self._canvas = tk.Canvas(self, background=self.sett.back_color, width=self.sett.width*self.sett.cell_width + 2*self.sett.padx,
                                 height=self.sett.height*self.sett.cell_width + 2*self.sett.pady)
        self._canvas.grid(row=1)
        
        for row in range(self.sett.height + 1):
            self._canvas.create_line(self._get_canvas_coord(row, 0), self._get_canvas_coord(row, self.sett.width),
                                     fill=self.sett.grid_color)
        for col in range(self.sett.width + 1):
            self._canvas.create_line(self._get_canvas_coord(0, col), self._get_canvas_coord(self.sett.height, col),
                                     fill=self.sett.grid_color)
        
        (statusbar_frame := ttk.Frame(self, relief="raised")).grid(row=2, sticky="EW", ipady=4)
        self._info_text = tk.StringVar()
        ttk.Label(statusbar_frame, textvariable=self._info_text, foreground="blue").pack(side="left", padx=4)
        self._rowcol_text = tk.StringVar()
        ttk.Label(statusbar_frame, textvariable=self._rowcol_text, foreground="blue").pack(side="right", padx=4)

        self._canvas.bind("<Motion>", self._on_mouse_move)
        self._canvas.bind("<Button-1>", self._on_mouse_click)

    # Ket thuc cung goi _start de bat dau lai
    def _start(self, info_text):
        self._playing = False
        self._canvas.delete(self._cur_cell_id)
        self._info_text.set(info_text)
        self._rowcol_text.set("")
        self._save_button.configure(state="disabled")
        self._undo_button.configure(state="disabled")
        self._redo_button.configure(state="disabled")

    def _start_game(self, info, cur_cell):
        self._canvas.delete(self._cur_cell_id)
        for move_id in self._moves_id:
            self._canvas.delete(move_id)
        for cell_id in self._cell_line_id:
            self._canvas.delete(cell_id)
            
        self._info = info
        self._redo_list = []
        self._cells = [[None for col in range(self.sett.width)] for row in range(self.sett.height)]
        self._moves_id = []
        for (isO, (row, col)) in info["moves"]:
            self._cells[row][col] = isO
            if isO:
                self._moves_id.append(self._canvas.create_text(self._get_canvas_coord(row, col, True),
                    fill=self.sett.O_color, text=self.sett.O_char, font=self.sett.XO_font))
            else:
                self._moves_id.append(self._canvas.create_text(self._get_canvas_coord(row, col, True),
                    fill=self.sett.X_color, text=self.sett.X_char, font=self.sett.XO_font))
        self._cur_cell_id = self._canvas.create_rectangle(self._get_canvas_coord(*cur_cell),
                            self._get_canvas_coord(cur_cell[0] + 1, cur_cell[1] + 1),
                            outline=self.sett.highlight_color, width=3)
        self._set_turn(self._info["O_turn"])
        self._playing = True
        self._save_button.configure(state="normal")
        self._undo_button.configure(state="normal" if self._info["moves"] else "disabled")
        self._redo_button.configure(state="disabled")

    def _get_canvas_coord(self, row, col, center=False):
        center_w = self.sett.cell_width//2 if center else 0
        return self.sett.padx + col*self.sett.cell_width + center_w, \
                self.sett.pady + row*self.sett.cell_width + center_w

    def _get_cell_coord(self, x, y):
        col = (x - self.sett.padx) // self.sett.cell_width
        row = (y - self.sett.pady) // self.sett.cell_width
        if row in range(self.sett.height) and col in range(self.sett.width):
            return row, col
        else:
            return None

    def _set_turn(self, O_turn):
        self._info["O_turn"] = O_turn
        if self._info["O_turn"]:
            self._info_text.set(self._info["O_name"] + "'s turn")
        else:
            self._info_text.set(self._info["X_name"] + "'s turn")

    def _create_XO(self, cell, isO):
        if isO:
            return self._canvas.create_text(self._get_canvas_coord(cell[0], cell[1], True),
                        fill=self.sett.O_color, text=self.sett.O_char, font=self.sett.XO_font)
        else:
            return self._canvas.create_text(self._get_canvas_coord(cell[0], cell[1], True),
                        fill=self.sett.X_color, text=self.sett.X_char, font=self.sett.XO_font)

    def _on_new(self):
        (new_dialog := caro_dialog.NewDialog(self, "New Game", 84, 200)).do_modal()
        if new_dialog.is_ok():
            if new_dialog.get_mode() == caro_dialog.NewDialog.MAN_VS_MAN:
                info = {}
                info["O_turn"] = new_dialog.is_O_first()
                info["O_name"] = new_dialog.get_1st_name() if new_dialog.is_O_first() else new_dialog.get_2nd_name()
                info["X_name"] = new_dialog.get_2nd_name() if new_dialog.is_O_first() else new_dialog.get_1st_name()
                info["moves"] = []
                self._start_game(info, (self.sett.width//2, self.sett.height//2))
            else:
                messagebox.showwarning(self.sett.title, "The chosen game mode is currently not available!")
            
    def _on_open(self):
        if (file := filedialog.askopenfile(parent=self, title="Open game from a JSON file",
                                                          filetypes=[("JSON File", "*.json")])):
            try:
                with file:
                    info = json.load(file)
                if not set(["O_turn", "O_name", "X_name", "moves"]) <= set(info.keys()):
                    raise Exception
                if info["moves"]:
                    self._start_game(info, info["moves"][-1][1])
                else:
                    self._start_game(info, (self.sett.width//2, self.sett.height//2))
            except:
                messagebox.showerror(self.sett.title, "Can not open the file!")

    def _on_save(self):
        if (file := filedialog.asksaveasfile(parent=self, title="Save game to a JSON file",
                                                          filetypes=[("JSON File", "*.json")])):
            try:
                with file:
                    json.dump(self._info, file)
            except:
                messagebox.showerror(self.sett.title, "Can not save the file!")

    def _on_settings(self):
        color_dict = {}
        color_dict["back_color"] = {"name": "Background", "color": self.sett.back_color}
        color_dict["highlight_color"] = {"name": "Highlight", "color": self.sett.highlight_color}
        color_dict["X_color"] = {"name": "X's", "color": self.sett.X_color}
        color_dict["O_color"] = {"name": "O's", "color": self.sett.O_color}
        (settings_dialog := caro_dialog.SettingsDialog(self, "Settings", 160, 200, color_dict)).do_modal()
        if settings_dialog.is_ok():
            color_dict = settings_dialog.get_color_dict()
            self.sett.back_color = color_dict["back_color"]["color"]
            self._canvas.configure(background=self.sett.back_color)
            self.sett.highlight_color = color_dict["highlight_color"]["color"]
            self._canvas.itemconfig(self._cur_cell_id, outline=self.sett.highlight_color)
            self.sett.X_color = color_dict["X_color"]["color"]
            self.sett.O_color = color_dict["O_color"]["color"]
            for index, XO_id in enumerate(self._moves_id):
                self._canvas.itemconfig(XO_id, fill=self.sett.O_color \
                                        if self._info["moves"][index][0] else self.sett.X_color)

    def _on_undo(self):
        if self._info["moves"]:
            turn, cell = self._info["moves"].pop()
            self._redo_list.append((turn, cell))
            self._cells[cell[0]][cell[1]] = None
            self._set_turn(not self._info["O_turn"])
            self._canvas.delete(self._moves_id.pop())
            if self._info["moves"]:
                cell = self._info["moves"][-1][1]
                self._canvas.coords(self._cur_cell_id, *self._get_canvas_coord(*cell),
                                *self._get_canvas_coord(cell[0] + 1, cell[1] + 1))
            else:
                self._undo_button.configure(state="disabled")
                self._canvas.itemconfigure(self._cur_cell_id, state="hidden")
                
            self._redo_button.configure(state="normal")

    def _on_redo(self):
        if self._redo_list:
            turn, cell = self._redo_list.pop()
            self._info["moves"].append((turn, cell))
            self._cells[cell[0]][cell[1]] = turn
            self._set_turn(not self._info["O_turn"])
            self._moves_id.append(self._create_XO(cell, turn))
            if not self._redo_list:
                self._redo_button.configure(state="disabled")
            self._canvas.coords(self._cur_cell_id, *self._get_canvas_coord(*cell),
                                *self._get_canvas_coord(cell[0] + 1, cell[1] + 1))
            self._canvas.itemconfigure(self._cur_cell_id, state="normal")
            self._undo_button.configure(state="normal")

    def _on_mouse_move(self, event):
        if self._playing and (cell := self._get_cell_coord(event.x, event.y)):
            # danh row, col theo kieu Excel A2 (row 2, col 1)
            if cell[1] in range(len(string.ascii_uppercase)):
                self._rowcol_text.set(f"{string.ascii_uppercase[cell[1]]}{cell[0] + 1}")
            self._canvas.coords(self._cur_cell_id, *self._get_canvas_coord(*cell),
                                *self._get_canvas_coord(cell[0] + 1, cell[1] + 1))
            if self._cells[cell[0]][cell[1]] == None:
                self._canvas.itemconfigure(self._cur_cell_id, state="normal")
            else:
                self._canvas.itemconfigure(self._cur_cell_id, state="hidden")

    def _on_mouse_click(self, event):
        if self._playing and (cell := self._get_cell_coord(event.x, event.y)) \
           and self._cells[cell[0]][cell[1]] == None:
            self._redo_list = [] # xoa redo
            self._redo_button.configure(state="disabled")
            self._undo_button.configure(state="normal")
            
            self._cells[cell[0]][cell[1]] = self._info["O_turn"]
            self._info["moves"].append((self._info["O_turn"], cell))
            self._moves_id.append(self._create_XO(cell, self._info["O_turn"]))
            self._set_turn(not self._info["O_turn"])

            if cell_line := self._check_win(cell, turn := not self._info["O_turn"]):
                winner_name = self._info["O_name"] if turn else self._info["X_name"]
                winner_char = self.sett.O_char if turn else self.sett.X_char
                winner_color = self.sett.O_color if turn else self.sett.X_color
                for cell in cell_line:
                    self._cell_line_id.append(self._canvas.create_rectangle(self._get_canvas_coord(*cell),
                            self._get_canvas_coord(cell[0] + 1, cell[1] + 1),
                            outline=winner_color, width=2))
                messagebox.showinfo(self.sett.title, f"{winner_name} wins!")
                self._start(f"{winner_char} wins! Press New to play new game or Open to open an existing game")
            elif len(self._info["moves"]) == self.sett.width*self.sett.height: # draw
                messagebox.showinfo(self.sett.title, "Draw!")
                self._start("Draw! Press New to play new game or Open to open an existing game")
                
    def _check_win(self, cell, turn):
        if len(cell_line := self._get_cell_line(cell, turn, 1, 0)) >= 5: # hang ngang -
            return cell_line
        if len(cell_line := self._get_cell_line(cell, turn, 0, 1)) >= 5: # hang doc |
            return cell_line
        if len(cell_line := self._get_cell_line(cell, turn, 1, 1)) >= 5: # hang cheo \
            return cell_line
        if len(cell_line := self._get_cell_line(cell, turn, 1, -1)) >= 5: # hang cheo /
            return cell_line
        return None

    def _get_cell_line(self, cell, turn, dx, dy):
        cell_line = []
        row, col = cell
        while row in range(self.sett.height) and col in range(self.sett.width) \
              and self._cells[row][col] == turn:
            cell_line.append((row, col))
            row, col = row + dy, col + dx
        row, col = cell[0] - dy, cell[1] - dx
        while row in range(self.sett.height) and col in range(self.sett.width) \
              and self._cells[row][col] == turn:
            cell_line.append((row, col))
            row, col = row - dy, col - dx
        return cell_line


if __name__ == "__main__":
    app = CaroGame()
    app.mainloop()
