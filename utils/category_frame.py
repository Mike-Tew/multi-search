from tkinter import ttk


class CategoryFrame(ttk.LabelFrame):
    """Class for wrapping search engine checkboxes into specific categories."""

    def __init__(self, parent, name, engines, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(text=name)

        self.vars = [var.variable for var in engines]
        for engine in engines:
            ttk.Checkbutton(
                self,
                width=14,
                style="Check.TCheckbutton",
                text=engine.name,
                variable=engine.variable,
            ).pack(anchor="w", padx=2, pady=2)

        self.select_btn = ttk.Button(
            self, style="Button.TButton", text="Select All", command=self._on_select
        )
        self.select_btn.pack(padx=10, pady=10)

        style = ttk.Style(self)
        style.configure("Button.TButton", font=("Helvetica", 12))
        style.configure("Check.TCheckbutton", font=("Helvetica", 11))

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
