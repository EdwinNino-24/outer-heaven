import random  # Importa el módulo random para generar números aleatorios
import math  # Importa el módulo math para funciones matemáticas


class NormalDistribution:
    """
    Genera números pseudoaleatorios con una distribución normal utilizando el método de Box-Muller.

    Args:
        mu (float): Media de la distribución normal.
        sigma (float): Desviación estándar de la distribución normal.
        quantity (int): Cantidad de números a generar.

    Methods:
        generate(): Genera una lista de números pseudoaleatorios con distribución normal.
    """

    def __init__(self, mu, sigma, quantity):
        """
        Inicializa la clase NormalDistribution.

        Args:
            mu (float): Media de la distribución.
            sigma (float): Desviación estándar de la distribución.
            quantity (int): Cantidad de números a generar.
        """
        self.mu = mu  # Almacena la media
        self.sigma = sigma  # Almacena la desviación estándar
        self.quantity = quantity  # Almacena la cantidad de números a generar
        self.results = []  # Inicializa una lista vacía para almacenar los resultados

    def generate(self):
        """
        Genera una lista de números pseudoaleatorios con distribución normal utilizando el método de Box-Muller.

        Returns:
            list: Una lista de listas, donde cada sublista contiene el valor de xi, el número aleatorio generado (Ri) y el valor mapeado (Ni).
        """
        while self.quantity > 0:  # Itera hasta generar la cantidad de números especificada
            u1 = random.random()  # Genera un número aleatorio uniforme entre 0 y 1
            u2 = random.random()  # Genera otro número aleatorio uniforme entre 0 y 1
            z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)  # Aplica la transformación de Box-Muller
            random_number = self.mu + z0 * self.sigma  # Calcula el número aleatorio con distribución normal

            xi = random.uniform(self.mu - 3 * self.sigma, self.mu + 3 * self.sigma)  # Genera un número aleatorio uniforme en el rango de la distribución
            Ri = (random_number - self.mu) / self.sigma  # Calcula el valor estandarizado (z-score)
            Ni = self.mu + xi * self.sigma  # Mapea el valor de xi a la distribución normal

            self.results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])  # Agrega los valores a la lista de resultados

            self.quantity -= 1  # Decrementa la cantidad de números restantes por generar

        return self.results  # Devuelve la lista de resultados
