import tkinter as tk
import webbrowser
from dataclasses import dataclass
from time import sleep
from tkinter import ttk


@dataclass
class SearchEngine:
    """Dataclass for storing search engine information."""

    name: str
    search_str: str
    category: str


search_engines = [
    SearchEngine("Google", "https://www.google.com/search?q=PARAM", "search"),
    SearchEngine(
        "GoodReads",
        "https://www.goodreads.com/search?utf8=%E2%9C%93&q=PARAM&search_type=books&search%5Bfield%5D=on",
        "search",
    ),
    SearchEngine(
        "Audible",
        "https://www.audible.com/search?keywords=PARAM&ref=a_search_t1_header_search",
        "search",
    ),
    SearchEngine("Amazon", "https://www.amazon.com/s?k=PARAM&ref=nb_sb_noss", "search"),
]


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quick Web Search")
        self.geometry("+1000+300")

        self.search_engines = {
            "Google": "https://www.google.com/search?q=PARAM",
            "GoodReads": "https://www.goodreads.com/search?utf8=%E2%9C%93&q=PARAM&search_type=books&search%5Bfield%5D=on",
            "Audible": "https://www.audible.com/search?keywords=PARAM&ref=a_search_t1_header_search",
            "Amazon": "https://www.amazon.com/s?k=PARAM&ref=nb_sb_noss",
        }
        self.checkbox_dict = {key: 0 for key in self.search_engines}

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
        for engine in self.search_engines:
            self.checkbox_dict[engine] = tk.IntVar()
            tk.Checkbutton(
                self.engine_frame, text=engine, variable=self.checkbox_dict[engine]
            ).pack()

        self.clear_button = tk.Button(
            self.engine_frame, text="Clear", command=self.show_values
        )
        self.clear_button.pack()
        # print(self.checkbox_dict)

    def show_values(self):
        print(self.checkbox_dict["Google"].get())
        print(self.checkbox_dict["Amazon"])

    def _on_search(self):
        search_params = self.search_box.get().strip()
        if len(search_params) == 0:
            return

        self.search_box.delete(0, tk.END)
        format_param = "+".join(search_params.split())
        for engine in self.search_engines.values():
            search_string = engine.replace("PARAM", format_param)
            webbrowser.open(search_string)
            sleep(0.05)

        self.destroy()


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
