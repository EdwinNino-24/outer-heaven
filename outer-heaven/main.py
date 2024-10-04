import tkinter as tk  # Importa la librería principal de tkinter
from tkinter import ttk  # Importa el módulo ttk para widgets temáticos
from tabs.tab_middle_squares import TabMiddleSquares  # Importa la clase para la pestaña de Cuadrados Medios
from tabs.tab_linear_congruence import TabLinearCongruence  # Importa la clase para la pestaña de Congruencia Lineal
from tabs.tab_multiplicative_congruence import TabMultiplicativeCongruence  # Importa la clase para la pestaña de Congruencia Multiplicativa
from tabs.tab_uniform_distribution import TabUniformDistribution  # Importa la clase para la pestaña de Distribución Uniforme
from tabs.tab_normal_distribution import TabNormalDistribution  # Importa la clase para la pestaña de Distribución Normal


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()  # Inicializa la clase padre (tk.Tk)
        self.title("Generación de Números PseudoAleatorios")  # Establece el título de la ventana
        self.geometry("1280x920")  # Establece el tamaño inicial de la ventana
        self.resizable(False, False)  # Impide que la ventana se pueda redimensionar

        self.notebook = ttk.Notebook(self)  # Crea un widget Notebook para pestañas
        self.notebook.pack(expand=True, fill="both")  # Coloca el Notebook en la ventana, expandiéndolo y llenando el espacio

        self.create_tabs()  # Llama al método para crear las pestañas

        self.update_idletasks()  # Actualiza la ventana para obtener las dimensiones reales
        window_width = self.winfo_width()  # Obtiene el ancho de la ventana
        window_height = self.winfo_height()  # Obtiene el alto de la ventana
        x = (self.winfo_screenwidth() // 2) - (window_width // 2)  # Calcula la posición x para centrar la ventana
        y = (self.winfo_screenheight() // 2) - (window_height // 2)  # Calcula la posición y para centrar la ventana
        self.geometry(f"+{x}+{y}")  # Establece la posición de la ventana en el centro de la pantalla

    def create_tabs(self):
        tab_middle_squares = TabMiddleSquares(self.notebook)  # Crea una instancia de la pestaña Cuadrados Medios
        self.notebook.add(tab_middle_squares, text="  Cuadrados Medios  ")  # Agrega la pestaña al Notebook

        tab_linearCongruence = TabLinearCongruence(self.notebook)  # Crea una instancia de la pestaña Congruencia Lineal
        self.notebook.add(tab_linearCongruence, text="  Congruencia Lineal  ")  # Agrega la pestaña al Notebook

        tab_multiplicativeCongruence = TabMultiplicativeCongruence(self.notebook)  # Crea una instancia de la pestaña Congruencia Multiplicativa
        self.notebook.add(tab_multiplicativeCongruence, text="  Congruencia Multiplicativa  ")  # Agrega la pestaña al Notebook

        tab_uniform_distribution = TabUniformDistribution(self.notebook)  # Crea una instancia de la pestaña Distribución Uniforme
        self.notebook.add(tab_uniform_distribution, text="  Distribución Uniforme  ")  # Agrega la pestaña al Notebook

        tab_normal_distribution = TabNormalDistribution(self.notebook)  # Crea una instancia de la pestaña Distribución Normal
        self.notebook.add(tab_normal_distribution, text="  Distribución Normal  ")  # Agrega la pestaña al Notebook


if __name__ == "__main__":
    app = MainApp()  # Crea una instancia de la aplicación principal
    app.mainloop()  # Inicia el bucle principal de la aplicación tkinter
