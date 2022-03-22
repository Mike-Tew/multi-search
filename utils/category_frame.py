import tkinter as tk
from tkinter import ttk


class CategoryFrame(ttk.LabelFrame):
    """Class for wrapping search engine checkboxes into specific categories."""

    def __init__(self, parent, name, engines, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(text=name)

        self.vars = [var.variable for var in engines]
        for engine in engines:
            tk.Checkbutton(self, text=engine.name, variable=engine.variable).pack(
                anchor="w"
            )

        self.select_btn = ttk.Button(
            self, text="Select All", command=self._on_select
        ).pack()

    def _on_select(self):
        var_values = [var.get() for var in self.vars]
        if not any(var_values):
            for var in self.vars:
                var.set(1)
        elif all(var_values):
            for var in self.vars:
                var.set(0)
        else:
            for var in self.vars:
                var.set(1)

