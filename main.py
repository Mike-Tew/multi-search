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
        self.search_button = tk.Button(
            self.search_frame, text="SEARCH", command=self._on_search
        )
        self.search_button.grid(row=0, column=1, padx=[0, 10])

        self.engine_frame = tk.LabelFrame(self, text="Search Engines")
        self.engine_frame.grid(row=1, column=0)

        self.search_engines = [
            SearchEngine(engine["name"], engine["search str"], engine["category"])
            for engine in search_engines
        ]

        for engine in self.search_engines:
            tk.Checkbutton(
                self.engine_frame, text=engine.name, variable=engine.variable
            ).pack()

        self.clear_button = tk.Button(
            self.engine_frame, text="Clear", command=self._on_clear
        )
        self.clear_button.pack()
        for engine in self.search_engines:
            print(engine)

    def _on_clear(self):
        print(self.search_engines[0].variable.get())

    def _on_search(self):
        search_params = self.search_box.get().strip()
        self.search_box.delete(0, tk.END)
        if len(search_params) == 0:
            return

        for engine in self.search_engines:
            print(engine.variable.get())
            if engine.variable.get():
                format_param = "+".join(search_params.split())
                search_string = engine.search_str.replace("PARAM", format_param)
                webbrowser.open(search_string)
                sleep(0.05)

        # self.destroy()




if __name__ == "__main__":
    gui = Gui(categories, search_engines)
    gui.mainloop()
