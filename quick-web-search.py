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
        self.geometry("+700+300")
        self.bind("<Return>", lambda x: self._on_search())

        self.search_frame = ttk.LabelFrame(self, text="Search")
        self.search_frame.grid(row=0, column=0, padx=10, pady=10)
        self.search_string = tk.StringVar()
        self.search_box = ttk.Entry(
            self.search_frame,
            textvariable=self.search_string,
            width=25,
            font=("Helvetica", 14),
        )
        self.search_box.grid(row=0, column=0, padx=10, pady=10)
        self.search_box.focus_set()

        self.search_button = ttk.Button(
            self.search_frame,
            text="SEARCH",
            command=self._on_search,
            style="Search.TButton",
        )
        self.search_button.grid(row=0, column=1, padx=[0, 10])

        self.scale_frame = ttk.LabelFrame(self, text="Search Speed")
        self.scale_frame.grid(row=0, column=1, sticky="W")
        self.scale_bar = ttk.Scale(self.scale_frame, from_=1.5, to=0.01, length=250)
        self.scale_bar.grid(row=0, column=0, padx=30, pady=5)
        self.scale_bar.set(0.5)

        ttk.Button(
            self, text="Clear All", command=self._on_clear, style="Clear.TButton"
        ).grid(row=0, column=2, sticky="W")

        self.search_engines = [
            SearchEngine(engine["name"], engine["search str"], engine["category"])
            for engine in search_engines
        ]

        cats_frame = ttk.Frame(self)
        cats_frame.grid(row=1, column=0, columnspan=3, padx=15, pady=[10, 20])

        for cat in categories:
            engines = [eng for eng in self.search_engines if eng.category == cat]
            CategoryFrame(cats_frame, cat, engines).pack(
                side=tk.LEFT, ipadx=10, padx=10
            )

        style = ttk.Style(self)
        style.configure("Search.TButton", font=("Open Sans", 15))
        style.configure("Clear.TButton", font=("Open Sans", 12))

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
