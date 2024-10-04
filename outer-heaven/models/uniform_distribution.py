import random  # Importa el módulo random para generar números aleatorios


class UniformDistribution:
    """
    Genera números pseudoaleatorios con una distribución uniforme.

    Args:
        min_value (float): Valor mínimo del rango de la distribución uniforme.
        max_value (float): Valor máximo del rango de la distribución uniforme.
        quantity (int): Cantidad de números a generar.

    Methods:
        generate(): Genera una lista de números pseudoaleatorios con distribución uniforme.
    """

    def __init__(self, min_value, max_value, quantity):
        """
        Inicializa la clase UniformDistribution.

        Args:
            min_value (float): Valor mínimo del rango.
            max_value (float): Valor máximo del rango.
            quantity (int): Cantidad de números a generar.
        """
        self.quantity = quantity  # Almacena la cantidad de números a generar
        self.min_value = min_value  # Almacena el valor mínimo del rango
        self.max_value = max_value  # Almacena el valor máximo del rango
        self.results = []  # Inicializa una lista vacía para almacenar los resultados

    def generate(self):
        """
        Genera una lista de números pseudoaleatorios con distribución uniforme.

        Returns:
            list: Una lista de listas, donde cada sublista contiene el valor de xi, el número aleatorio generado (Ri) y el valor mapeado (Ni).
        """
        while self.quantity > 0:  # Itera hasta generar la cantidad de números especificada
            random_number = random.uniform(self.min_value, self.max_value)  # Genera un número aleatorio uniforme en el rango especificado
            xi = float(random_number) / 10000.0  # Escala el número aleatorio (este paso parece innecesario y podría eliminarse)
            Ri = float(random_number) / 10000.0  # Escala el número aleatorio (este paso parece innecesario y podría eliminarse)
            Ni = self.min_value + (self.max_value - self.min_value) * xi  # Mapea el valor de xi al rango especificado

            self.results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])  # Agrega los valores a la lista de resultados

            self.quantity -= 1  # Decrementa la cantidad de números restantes por generar

        return self.results  # Devuelve la lista de resultados
