import matplotlib.pyplot as plt  # Importa la librería matplotlib para la generación de gráficos


class PseudoRandomNumberVisualizer:
    """
    Clase para visualizar los números pseudoaleatorios generados.

    Args:
        results (list): Lista de resultados generados por el método de Cuadrados Medios.
                       Cada elemento de la lista debe ser una lista con tres valores: [xi, Ri, Ni].
    """

    def __init__(self, results):
        """Inicializa la clase con los resultados generados."""
        self.results = results

    def plot_histogram(self):
        """Grafica un histograma de los valores de Ni."""
        ni_values = [row[2] for row in self.results]  # Extrae los valores de Ni de los resultados

        plt.hist(ni_values, bins='auto', alpha=0.7, rwidth=0.85)  # Crea el histograma
        plt.title('Distribución de Números Pseudoaleatorios (Método de Cuadrados Medios)')  # Establece el título del gráfico
        plt.xlabel('Ni')  # Establece la etiqueta del eje x
        plt.ylabel('Frecuencia')  # Establece la etiqueta del eje y
        plt.grid(axis='y', alpha=0.75)  # Agrega una cuadrícula al gráfico
        plt.show()  # Muestra el gráfico

    def plot_scatter(self):
        """Grafica un diagrama de dispersión de Ri vs. posición."""
        positions = range(1, len(self.results) + 1)  # Genera una lista de posiciones
        ri_values = [row[1] for row in self.results]  # Extrae los valores de Ri de los resultados

        plt.scatter(positions, ri_values)  # Crea el diagrama de dispersión
        plt.title('Relación Ri vs. Posición (Método de Cuadrados Medios)')  # Establece el título del gráfico
        plt.xlabel('Posición')  # Establece la etiqueta del eje x
        plt.ylabel('Ri')  # Establece la etiqueta del eje y
        plt.grid(True)  # Agrega una cuadrícula al gráfico
        plt.show()  # Muestra el gráfico

    def plot_line(self):
        """Grafica un gráfico de línea de Ni vs. posición."""
        positions = range(1, len(self.results) + 1)  # Genera una lista de posiciones
        ni_values = [row[2] for row in self.results]  # Extrae los valores de Ni de los resultados

        plt.plot(positions, ni_values)  # Crea el gráfico de línea
        plt.title('Evolución de Números Pseudoaleatorios (Método de Cuadrados Medios)')  # Establece el título del gráfico
        plt.xlabel('Posición')  # Establece la etiqueta del eje x
        plt.ylabel('Ni')  # Establece la etiqueta del eje y
        plt.grid(True)  # Agrega una cuadrícula al gráfico
        plt.show()  # Muestra el gráfico

    def plot_collage(self):
        """Crea un collage con las tres gráficas en una figura."""
        ni_values = [row[2] for row in self.results]  # Extrae los valores de Ni de los resultados
        ri_values = [row[1] for row in self.results]  # Extrae los valores de Ri de los resultados
        positions = range(1, len(self.results) + 1)  # Genera una lista de posiciones

        # Crear figura con 3 subplots
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Crea una figura con 2 filas y 2 columnas de subplots

        # Gráfico 1: Histograma
        axs[0, 0].hist(ni_values, bins='auto', alpha=0.7, rwidth=0.85)  # Crea el histograma en el subplot (0, 0)
        axs[0, 0].set_title('Histograma de Ni')  # Establece el título del subplot
        axs[0, 0].set_xlabel('Ni')  # Establece la etiqueta del eje x
        axs[0, 0].set_ylabel('Frecuencia')  # Establece la etiqueta del eje y
        axs[0, 0].grid(axis='y', alpha=0.75)  # Agrega una cuadrícula al subplot

        # Gráfico 2: Diagrama de dispersión
        axs[0, 1].scatter(positions, ri_values)  # Crea el diagrama de dispersión en el subplot (0, 1)
        axs[0, 1].set_title('Diagrama de Dispersión Ri vs. Posición')  # Establece el título del subplot
        axs[0, 1].set_xlabel('Posición')  # Establece la etiqueta del eje x
        axs[0, 1].set_ylabel('Ri')  # Establece la etiqueta del eje y
        axs[0, 1].grid(True)  # Agrega una cuadrícula al subplot

        # Gráfico 3: Gráfico de línea
        axs[1, 0].plot(positions, ni_values)  # Crea el gráfico de línea en el subplot (1, 0)
        axs[1, 0].set_title('Gráfico de Línea Ni vs. Posición')  # Establece el título del subplot
        axs[1, 0].set_xlabel('Posición')  # Establece la etiqueta del eje x
        axs[1, 0].set_ylabel('Ni')  # Establece la etiqueta del eje y
        axs[1, 0].grid(True)  # Agrega una cuadrícula al subplot

        # Eliminar el subplot vacío
        fig.delaxes(axs[1, 1])  # Elimina el subplot (1, 1) que no se utiliza

        # Ajustar el layout para que los subplots no se superpongan
        plt.tight_layout()  # Ajusta el layout para evitar superposiciones
        plt.show()  # Muestra la figura con los subplots
