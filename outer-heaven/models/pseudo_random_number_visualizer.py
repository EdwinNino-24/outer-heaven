import matplotlib.pyplot as plt

class PseudoRandomNumberVisualizer:
    def __init__(self, results):
        """Inicializa la clase con los resultados generados."""
        self.results = results

    def plot_histogram(self):
        """Grafica un histograma de los valores de Ni."""
        ni_values = [row[2] for row in self.results]

        plt.hist(ni_values, bins='auto', alpha=0.7, rwidth=0.85)
        plt.title('Distribución de Números Pseudoaleatorios (Método de Cuadrados Medios)')
        plt.xlabel('Ni')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

    def plot_scatter(self):
        """Grafica un diagrama de dispersión de Ri vs. posición."""
        positions = range(1, len(self.results) + 1)
        ri_values = [row[1] for row in self.results]

        plt.scatter(positions, ri_values)
        plt.title('Relación Ri vs. Posición (Método de Cuadrados Medios)')
        plt.xlabel('Posición')
        plt.ylabel('Ri')
        plt.grid(True)
        plt.show()

    def plot_line(self):
        """Grafica un gráfico de línea de Ni vs. posición."""
        positions = range(1, len(self.results) + 1)
        ni_values = [row[2] for row in self.results]

        plt.plot(positions, ni_values)
        plt.title('Evolución de Números Pseudoaleatorios (Método de Cuadrados Medios)')
        plt.xlabel('Posición')
        plt.ylabel('Ni')
        plt.grid(True)
        plt.show()

    def plot_collage(self):
        """Crea un collage con las tres gráficas en una figura."""
        ni_values = [row[2] for row in self.results]
        ri_values = [row[1] for row in self.results]
        positions = range(1, len(self.results) + 1)

        # Crear figura con 3 subplots
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))

        # Gráfico 1: Histograma
        axs[0, 0].hist(ni_values, bins='auto', alpha=0.7, rwidth=0.85)
        axs[0, 0].set_title('Histograma de Ni')
        axs[0, 0].set_xlabel('Ni')
        axs[0, 0].set_ylabel('Frecuencia')
        axs[0, 0].grid(axis='y', alpha=0.75)

        # Gráfico 2: Diagrama de dispersión
        axs[0, 1].scatter(positions, ri_values)
        axs[0, 1].set_title('Diagrama de Dispersión Ri vs. Posición')
        axs[0, 1].set_xlabel('Posición')
        axs[0, 1].set_ylabel('Ri')
        axs[0, 1].grid(True)

        # Gráfico 3: Gráfico de línea
        axs[1, 0].plot(positions, ni_values)
        axs[1, 0].set_title('Gráfico de Línea Ni vs. Posición')
        axs[1, 0].set_xlabel('Posición')
        axs[1, 0].set_ylabel('Ni')
        axs[1, 0].grid(True)

        # Eliminar el subplot vacío
        fig.delaxes(axs[1, 1])

        # Ajustar el layout para que los subplots no se superpongan
        plt.tight_layout()
        plt.show()