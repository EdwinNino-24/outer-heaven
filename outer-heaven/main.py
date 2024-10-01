import tkinter as tk
from tkinter import ttk
from tabs.tab_middle_squares import TabMiddleSquares  
from tabs.tab_linear_congruence import TabLinearCongruence
from tabs.tab_multiplicative_congruence import TabMultiplicativeCongruence
from tabs.tab_uniform_distribution import TabUniformDistribution
from tabs.tab_normal_distribution import TabNormalDistribution

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generación de Números PseudoAleatorios")
        self.geometry("1280x920")
        self.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_tabs()
        
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (window_width // 2)
        y = (self.winfo_screenheight() // 2) - (window_height // 2)
        self.geometry(f"+{x}+{y}")

    def create_tabs(self):
        tab_middle_squares = TabMiddleSquares(self.notebook)
        self.notebook.add(tab_middle_squares, text="  Cuadrados Medios  ")

        tab_linearCongruence = TabLinearCongruence(self.notebook)
        self.notebook.add(tab_linearCongruence, text="  Congruencia Lineal  ")
        
        tab_multiplicativeCongruence = TabMultiplicativeCongruence(self.notebook)
        self.notebook.add(tab_multiplicativeCongruence, text="  Congruencia Multiplicativa  ")
        
        tab_uniform_distribution = TabUniformDistribution(self.notebook)
        self.notebook.add(tab_uniform_distribution, text="  Distribución Uniforme  ")
        
        tab_normal_distribution = TabNormalDistribution(self.notebook)
        self.notebook.add(tab_normal_distribution, text="  Distribución Normal  ")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()