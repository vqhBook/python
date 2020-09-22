import tkinter as tk
from tkinter import ttk, messagebox, filedialog

import student_widgets as sw
import student_data_model as sdm

class Application(tk.Tk):
    _TITLE = "Students Management"
    _COLUMNS = {
            "sid": {"text": "MSSV"},
            "name": {"text": "Họ tên", "anchor": "w", "stretch": True, "width": 200, "minwidth": 150},
            "gender": {"text": "Giới tính"},
            "grade": {"text": "Điểm", "anchor": "e", "numeric": True},
        }
    
    def __init__(self, title=_TITLE, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.geometry("500x590")
        self._has_change = False    # Cho biết có thay đổi (để báo khi New, Save)
        
        self._create_widgets()

        self._on_new()

    def _create_widgets(self):
        self._slist_view = sw.StudentsListView(self, text="Students List", COLUMNS=Application._COLUMNS,
            student_edit_handler=self._on_student_edit, sid_list_change_handler=self._on_sid_list_change,
            student_delete_handler=self._on_student_delete)
        self._slist_view.grid(row=0, column=0, sticky="WENS")
        
        self._sadd_panel = sw.StudentAddUpdatePanel(self, text="Add/Edit Student", sid_change_handler=self._on_sid_change,
            student_add_or_update_handler=self._on_student_add_or_update, error_handler=self._on_error_handler)
        self._sadd_panel.grid(row=1, column=0, sticky="EW")
        
        self._status_bar = sw.StatusBar(self)
        self._status_bar.grid(row=2, column=0, sticky="EW")
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        for child in self.winfo_children():
            child.grid(padx=4, pady=2)

        self._create_menu()

    def _create_menu(self):
        main_menu = tk.Menu(self)
        self.configure(menu=main_menu)
        
        self._file_menu = tk.Menu(main_menu, tearoff=False)
        self._file_menu.add_command(label="New", accelerator="Ctrl+N", command=self._on_new)
        self._file_menu.add_command(label="Open...", accelerator="Ctrl+O", command=self._on_open)
        self._file_menu.add_command(label="Save As...", accelerator="Ctrl+S", command=self._on_save_as)
        self._file_menu.add_separator()
        self._file_menu.add_command(label="Exit", accelerator="Alt+F4", command=self._on_exit)

        help_menu = tk.Menu(main_menu, tearoff=False)
        help_menu.add_command(label = "About...", accelerator="F1", command=self._on_about)

        main_menu.add_cascade(label="File", menu=self._file_menu)
        main_menu.add_cascade(label="Help", menu=help_menu)

        self.bind("<Control-n>", self._on_new)
        self.bind("<Control-N>", self._on_new)
        self.bind("<Control-o>", self._on_open)
        self.bind("<Control-O>", self._on_open)
        self.bind("<F1>", self._on_about)

        self._set_save_as_state(False)

        self.protocol("WM_DELETE_WINDOW", self._on_exit)

    def _ask_save_changes(self):
        if self._has_change and self._slist_view.get_students_len() > 0:
            if (answer := messagebox.askyesnocancel(Application._TITLE, "Do you want to save changes?")) is None:
                return True

            if answer and not self._on_save_as():
                return True
        return False

    # Tao moi (xoa), hoi luu khi co thay doi
    def _on_new(self, event=None):
        if self._ask_save_changes():
            return
            
        self._slist_view.clear()
        self._sadd_panel.clear()
        self._status_bar.set_text("Enter new data and/or open data from CSV file.")
        self._has_change = False

    def _on_open(self, event=None):
        if self._ask_save_changes():
            return
        
        if not (file_name := filedialog.askopenfilename(parent=self, title="Open a CSV student file",
                                                        filetypes=[("CSV File", "*.csv")])):
            return
        
        if (students := sdm.open_student_file(file_name, list(Application._COLUMNS))):
            if self._slist_view.get_students_len() > 0:
                if messagebox.askyesno(Application._TITLE, "Do you want to clear current student list?"):
                    self._slist_view.clear()
                    self._has_change = False
                else:
                    self._has_change = True
            self._sadd_panel.clear()
            self._slist_view.insert_or_replace(students)
            self._status_bar.set_text(f"Open {self._slist_view.get_students_len()} student(s) successfully.")
        else:
            self._status_bar.set_text_error("Can not open the file or the file is invalid!")

    def _on_save_as(self, event=None):
        if not (file_name := filedialog.asksaveasfilename(parent=self, title="Save to a CSV student file",
                                                          filetypes=[("CSV File", "*.csv")])):
            return False
        
        if sdm.save_student_file(file_name, list(Application._COLUMNS), self._slist_view.get_students()):
            self._status_bar.set_text(f"Save {self._slist_view.get_students_len()} student(s) successfully.")
            self._has_change = False
            return True
        self._status_bar.set_text_error("Can not save data to the file!")
        return False
    
    def _on_exit(self, event=None):
        if self._ask_save_changes():
            return
        self.destroy()

    def _on_about(self, event=None):
        messagebox.showinfo(title="About " + Application._TITLE, message=Application._TITLE + " Application",
                               detail="Version: 0.0.1\nAuthor: Vũ Quốc Hoàng\nE-mail: vqhoang@fit.hcmus.edu.vn")

    def _set_save_as_state(self, normal):
        if normal:
            self._file_menu.entryconfig(2, state="normal")
            self.bind("<Control-s>", self._on_save_as)
            self.bind("<Control-S>", self._on_save_as)
        else:
            self._file_menu.entryconfig(2, state="disabled")
            self.unbind("<Control-s>")
            self.unbind("<Control-S>")

    def _on_student_edit(self, student):
        student["gender"] = True if student["gender"] == "Nam" else False
        self._sadd_panel.set_student(student)

    def _on_student_delete(self, delete_sids):
        self._status_bar.set_text(f"Delete {len(delete_sids)} student(s) successfully.")
        self._has_change = True

    def _on_sid_list_change(self, sid_list):
        self._sadd_panel.set_sid_list(sid_list)
        self._set_save_as_state(bool(sid_list))

    def _on_sid_change(self, sid):
        self._slist_view.choose(sid)

    def _on_student_add_or_update(self, student, added):
        student["gender"] = "Nam" if student["gender"] else "Nữ"
        self._slist_view.insert_or_replace([student])
        self._slist_view.choose(student["sid"])
        if added:
            self._status_bar.set_text("Add 1 student successfully.")
        else:
            self._status_bar.set_text("Update 1 student successfully.")
        self._has_change = True

    def _on_error_handler(self, error_message):
        self._status_bar.set_text_error(error_message)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
