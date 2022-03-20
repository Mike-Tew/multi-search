# TODO
# Improve styling
# Add a Clear All button
# Add an opening speed slider with tooltip

import tkinter as tk
import webbrowser
from dataclasses import dataclass
from time import sleep
from tkinter import ttk

from search_engines import categories, search_engines


@dataclass
class SearchEngine:
    """Dataclass for storing search engine information."""

    name: str
    search_str: str
    category: str

    def __post_init__(self):
        self.variable = tk.IntVar()


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


class Gui(tk.Tk):
    def __init__(self, categories, search_engines):
        super().__init__()
        self.title("Quick Web Search")
        self.geometry("+1000+300")

        self.search_frame = tk.LabelFrame(self, text="Search")
        self.search_frame.grid(row=0, column=0, padx=10, pady=10)
        self.search_box = tk.Entry(self.search_frame)
        self.search_box.grid(row=0, column=0, padx=10, pady=10)
        self.search_box.bind("<Return>", lambda x: self._on_search())
        self.search_box.focus_set()

        self.search_button = ttk.Button(
            self.search_frame, text="SEARCH", command=self._on_search
        )
        self.search_button.grid(row=0, column=1, padx=[0, 10])

        self.search_engines = [
            SearchEngine(engine["name"], engine["search str"], engine["category"])
            for engine in search_engines
        ]

        ttk.Button(self, text="Clear All", command=self._on_clear).grid(row=0, column=1)

        self.scale_bar = ttk.Scale(self, from_=1, to=150)
        self.scale_bar.grid(row=0, column=2)
        self.scale_bar.set(50)

        cats_frame = tk.Frame(self)
        cats_frame.grid(row=1, column=0, columnspan=3)

        for cat in categories:
            engines = [eng for eng in self.search_engines if eng.category == cat]
            CategoryFrame(cats_frame, cat, engines).pack(
                side=tk.LEFT, ipadx=10, padx=10
            )

    def _on_clear(self):
        for engine in self.search_engines:
            engine.variable.set(0)

    def _on_search(self):
        search_params = self.search_box.get().strip()
        self.search_box.delete(0, tk.END)
        if len(search_params) == 0:
            return

        for engine in self.search_engines:
            if not engine.variable.get():
                continue

            format_param = "+".join(search_params.split())
            search_string = engine.search_str.replace("PARAM", format_param)
            webbrowser.open(search_string)
            sleep(self.scale_bar.get() / 100)

        # self.destroy()


if __name__ == "__main__":
    gui = Gui(categories, search_engines)
    gui.mainloop()
