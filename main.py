from tkinter import Tk, LabelFrame, Entry, Button, Label, Checkbutton, IntVar, END
from time import sleep
import webbrowser


class Gui(Tk):
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

        self.search_frame = LabelFrame(self, text="Search")
        self.search_frame.grid(row=0, column=0, padx=10, pady=10)
        self.search_box = Entry(self.search_frame)
        self.search_box.grid(row=0, column=0, padx=10, pady=10)
        self.search_box.bind("<Return>", lambda x: self.perform_search())
        self.search_box.focus_set()
        self.search_button = Button(
            self.search_frame, text="SEARCH", command=self.perform_search
        )
        self.search_button.grid(row=0, column=1, padx=[0, 10])

        self.engine_frame = LabelFrame(self, text="Search Engines")
        self.engine_frame.grid(row=1, column=0)
        for engine in self.search_engines:
            self.checkbox_dict[engine] = IntVar()
            c = Checkbutton(
                self.engine_frame, text=engine, variable=self.checkbox_dict[engine]
            ).pack()

        self.clear_button = Button(
            self.engine_frame, text="Clear", command=self.show_values
        )
        self.clear_button.pack()
        print(self.checkbox_dict)

    def show_values(self):
        print(self.checkbox_dict["Google"].get())
        print(self.checkbox_dict["Amazon"])

    def perform_search(self):
        search_params = self.search_box.get().strip()
        self.search_box.delete(0, END)
        if len(search_params) != 0:
            format_param = "+".join(search_params.split())
            for engine in self.search_engines.values():
                search_string = engine.replace("PARAM", format_param)
                webbrowser.open(search_string)
                sleep(0.05)

            self.destroy()


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
