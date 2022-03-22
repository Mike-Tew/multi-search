# TODO
# Improve styling

import tkinter as tk
import webbrowser
from time import sleep
from tkinter import ttk

from search_engine_data import categories, search_engines
from utils.search_engine_class import SearchEngine
from utils.category_frame import CategoryFrame


class Gui(tk.Tk):
    def __init__(self, categories, search_engines):
        super().__init__()
        self.title("Quick Web Search")
        self.geometry("+1000+300")

        self.search_frame = tk.LabelFrame(self, text="Search")
        self.search_frame.grid(row=0, column=0, padx=10, pady=10)
        self.search_string = tk.StringVar()
        self.search_box = tk.Entry(self.search_frame, textvariable=self.search_string)
        self.search_box.grid(row=0, column=0, padx=10, pady=10)
        self.search_box.bind("<Return>", lambda x: self._on_search())
        self.search_box.focus_set()

        self.search_button = ttk.Button(
            self.search_frame, text="SEARCH", command=self._on_search
        )
        self.search_button.grid(row=0, column=1, padx=[0, 10])

        ttk.Button(self, text="Clear All", command=self._on_clear).grid(row=0, column=1)

        self.scale_bar = ttk.Scale(self, from_=0.01, to=1.5)
        self.scale_bar.grid(row=0, column=2)
        self.scale_bar.set(0.5)

        self.search_engines = [
            SearchEngine(engine["name"], engine["search str"], engine["category"])
            for engine in search_engines
        ]

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
        search_text = self.search_string.get().strip()
        if len(search_text) == 0:
            return

        for engine in self.search_engines:
            if not engine.variable.get():
                continue

            format_param = "+".join(search_text.split())
            search_string = engine.search_str.replace("PARAM", format_param)
            webbrowser.open(search_string)
            sleep(self.scale_bar.get())


if __name__ == "__main__":
    gui = Gui(categories, search_engines)
    gui.mainloop()