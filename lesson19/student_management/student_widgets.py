import tkinter as tk
from tkinter import ttk

class StatusBar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(relief="groove")
        
        self._create_widgets()
        
    def _create_widgets(self):
        self._status_label = ttk.Label(self, text="", foreground="blue")
        self._status_label.grid(padx=2, pady=2, sticky="W")

    def set_text(self, text):
        self._status_label.configure(text=text, foreground="blue")

    def set_text_error(self, text):
        self._status_label.configure(text=text, foreground="red")

    def clear(self):
        self._status_label.configure(text="")
        

class StudentsListView(ttk.LabelFrame):
    # COLUMNS là danh sách các cột, sid (MSSV) là khóa chính
    def __init__(self, parent, COLUMNS, student_edit_handler=None, sid_list_change_handler=None,
                 student_delete_handler=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._COLUMNS = COLUMNS
        self._student_edit_handler = student_edit_handler
        self._sid_list_change_handler = sid_list_change_handler
        self._student_delete_handler = student_delete_handler
        
        self._create_widgets()

    def _create_widgets(self):
        self._list_view = ttk.Treeview(self, columns=list(self._COLUMNS), selectmode="extended")
        self._list_view.grid(row=0, column=0, columnspan=5, sticky="EWNS")
        self._list_view.column("#0", stretch=False, width=0, minwidth=0)
        for column, info in self._COLUMNS.items():
            self._list_view.heading(column, text=info.get("text", ""), anchor=info.get("anchor", "center"),
                                    command=self._on_sort(column))
            self._list_view.column(column, stretch=info.get("stretch", False), anchor=info.get("anchor", "center"),
                                  width=info.get("width", 80), minwidth=info.get("minwidth", 60))
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self._list_view.yview)
        scrollbar.grid(row=0, column=5, sticky="WNS")
        self._list_view.configure(yscrollcommand=scrollbar.set)
        self._list_view.bind("<<TreeviewOpen>>", self._on_open_items)
        self._list_view.bind("<<TreeviewSelect>>", self._on_select_change)
        self._list_view.bind("<Control-a>", self._on_select_all)
        self._list_view.bind("<Control-A>", self._on_select_all)
        self._list_view.bind("<Delete>", self._on_delete)
        
        ttk.Label(self, text="Sort:").grid(row=1, column=0, sticky="E")
        self._descending = tk.BooleanVar()
        ttk.Checkbutton(self, text="Descending", variable=self._descending).grid(row=1, column=1, sticky="W")
        
        self._delete_button = ttk.Button(self, text="Delete", state="disabled", command=self._on_delete)
        self._delete_button.grid(row=1, column=3)
        self._edit_button = ttk.Button(self, text="Edit", state="disabled", command=self._on_open_items)
        self._edit_button.grid(row=1, column=4, columnspan=2)
        
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        for child in self.winfo_children():
            child.grid(padx=2, pady=2)

    def _on_sort(self, column):
        def sort():
            items = list(self._list_view.get_children())
            if self._COLUMNS[column].get("numeric", False):
                items.sort(reverse=self._descending.get(), key=lambda x: float(self._list_view.set(x, column)))
            else:
                items.sort(reverse=self._descending.get(), key=lambda x: self._list_view.set(x, column))
            for index, iid in enumerate(items):
                self._list_view.move(iid, self._list_view.parent(iid), index)

        return sort
        
    def _on_open_items(self, *args):
        if selected_sids := self._list_view.selection():
            if self._student_edit_handler:
                student = {column: self._list_view.set(selected_sids[0], column) for column in self._COLUMNS}
                self._student_edit_handler(student)

    def _on_select_all(self, *args):
        self._list_view.selection_set(*self._list_view.get_children())

    def _on_delete(self, event=None):
        if sel_list := self._list_view.selection():
            self._list_view.delete(*sel_list)
            if self._sid_list_change_handler:
                self._sid_list_change_handler(self._list_view.get_children())
            if self._student_delete_handler:
                self._student_delete_handler(sel_list)
        
    def _on_select_change(self, *args):
        self._delete_button.configure(state="normal" if len(self._list_view.selection()) > 0 else "disabled")
        self._edit_button.configure(state="normal" if len(self._list_view.selection()) > 0 else "disabled")

    # chon student voi sid (neu co), khong thi bo chon
    def choose(self, sid):
        if self._list_view.exists(sid):
            self._list_view.selection_set(sid)
            self._list_view.see(sid)
        else:
            self._list_view.selection_set()

    # xoa het cac dong
    def clear(self):
        if sel_list := self._list_view.get_children():
            self._list_view.delete(*sel_list)
            if self._sid_list_change_handler:
                self._sid_list_change_handler(self._list_view.get_children())
            if self._student_delete_handler:
                self._student_delete_handler(sel_list)

    # them nhieu sinh vien neu chua co (sid) va thay the neu da co
    def insert_or_replace(self, students):
        for student in students:
            if self._list_view.exists(student["sid"]):
                for column in self._COLUMNS:
                    self._list_view.set(student["sid"], column, student[column])
            else:
                self._list_view.insert("", "end", iid=student["sid"], values=list(student.values()))
        if self._sid_list_change_handler:
            self._sid_list_change_handler(self._list_view.get_children())
    
    # lay so luong sinh vien (row), hieu qua hon lay danh sach
    def get_students_len(self):
        return len(self._list_view.get_children())

    # Lay danh sách các student (moi student la mot dict cac string)
    def get_students(self):
        students = []
        for sid in self._list_view.get_children():
            student = {}
            for column in self._COLUMNS:
                student[column] = self._list_view.set(sid, column)
            students.append(student)
        return students

# Đặt trùng tên _name sửa thành _namevar
class StudentAddUpdatePanel(ttk.LabelFrame):
    # Thông báo: sid_change (khi khóa chính là MSSV thay đổi), student_add_or_update, error_handler
    def __init__(self, parent, sid_change_handler=None, student_add_or_update_handler=None,
                 error_handler=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._sid_change_handler = sid_change_handler
        self._student_add_or_update_handler = student_add_or_update_handler
        self._error_handler = error_handler
        self._sid_list = [] # danh sách các MSSV đã có (để quyết định là add hay update)
        
        self._create_widgets()

    def _create_widgets(self):
        self._sid = tk.StringVar()
        self._sid.trace("w", self._on_sid_change)
        self._namevar = tk.StringVar()
        self._gender = tk.BooleanVar()  # gioi tinh: True la Name
        self._grade = tk.StringVar()    # diem
        self._add_update_text = tk.StringVar() # add or update
        
        ttk.Label(self, text="MSSV:").grid(row=0, column=0, sticky="E")
        ttk.Label(self, text="Họ tên:").grid(row=0, column=2, sticky="E")
        ttk.Label(self, text="Điểm:").grid(row=1, column=0, sticky="E")
        ttk.Label(self, text="Giới tính:").grid(row=1, column=2, sticky="E")
        
        self._sid_entry = ttk.Combobox(self, width=10, textvariable=self._sid)
        self._sid_entry.grid(row=0, column=1, sticky="W")
        name_entry = ttk.Entry(self, textvariable=self._namevar)
        name_entry.grid(row=0, column=3, columnspan=3, sticky="WE")
        grade_entry = ttk.Spinbox(self, width=4, values=[i/2 for i in range(0, 21)], textvariable=self._grade)
        grade_entry.grid(row=1, column=1, sticky="W")
        gender_checkbox = ttk.Checkbutton(self, text="Nam", variable=self._gender)
        gender_checkbox.grid(row=1, column=3, sticky="W")
        ttk.Button(self, text="Clear", command=self._on_clear).grid(row=1, column=4)
        ttk.Button(self, textvariable=self._add_update_text, command=self._on_add_update).grid(row=1, column=5)

        for widget in [self._sid_entry, name_entry, grade_entry, gender_checkbox]:
            widget.bind("<Return>", self._on_add_update)
        
        self.columnconfigure(3, weight=1)

        for child in self.winfo_children():
            child.grid(padx=2, pady=2)
            
    def _on_sid_change(self, *args):
        self._add_update_text.set("Update" if self._sid.get() in self._sid_list else "Add")
        if self._sid_change_handler:
            self._sid_change_handler(self._sid.get())

    def _on_add_update(self, event=None):
        try:
            if self._sid.get() == "":
                raise Exception("Student ID must be not empty!")
            if self._namevar.get() == "":
                raise Exception("Student name must be not empty!")
            if self._grade.get() not in [str(i/2) for i in range(0, 21)] + [str(i) for i in range(11)]:
                raise Exception("Student grade is not valid!")
            student = {}
            student["sid"] = self._sid.get()
            student["name"] = self._namevar.get()
            student["gender"] = self._gender.get()
            student["grade"] = self._grade.get()
            added = self._sid.get() not in self._sid_list
            if self._student_add_or_update_handler:
                self._student_add_or_update_handler(student, added)
            self._sid_entry.focus_set()
        except Exception as e:
            if self._error_handler:
                self._error_handler(str(e))

    def _on_clear(self):
        self.set_student({})
        
    def clear(self):
        self.set_sid_list([])
        self.set_student({})

    # dat cac gia tri tu dict
    def set_student(self, value):
        self._sid.set(value.get("sid", ""))
        self._namevar.set(value.get("name", ""))
        self._gender.set(value.get("gender", False))
        self._grade.set(value.get("grade", ""))
        
    # dat danh sach cac sid
    def set_sid_list(self, sid_list):
        self._sid_list = sid_list
        self._sid_entry.configure(values=self._sid_list)
        self._sid.set("")
