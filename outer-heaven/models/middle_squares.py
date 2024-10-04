class MiddleSquares:
    """
    Genera números pseudoaleatorios utilizando el método de los cuadrados medios.

    Args:
        seed (int): Semilla inicial para el generador.
        num_iterations (int): Número de iteraciones (cantidad de números a generar).
        n_digits (int): Número de dígitos a considerar en cada iteración.
        a (float): Límite inferior del intervalo de mapeo.
        b (float): Límite superior del intervalo de mapeo.

    Methods:
        generate(): Genera una lista de números pseudoaleatorios.
    """

    def __init__(self, seed, num_iterations, n_digits, a, b):
        """
        Inicializa la clase MiddleSquares.

        Args:
            seed (int): Semilla inicial.
            num_iterations (int): Número de iteraciones.
            n_digits (int): Número de dígitos.
            a (float): Límite inferior del intervalo.
            b (float): Límite superior del intervalo.
        """
        self.seed = seed  # Almacena la semilla inicial
        self.num_iterations = num_iterations  # Almacena el número de iteraciones
        self.n_digits = n_digits  # Almacena el número de dígitos
        self.a = a  # Almacena el límite inferior del intervalo
        self.b = b  # Almacena el límite superior del intervalo

    def generate(self):
        """
        Genera una lista de números pseudoaleatorios utilizando el método de los cuadrados medios.

        Returns:
            list: Una lista de listas, donde cada sublista contiene la semilla, el número aleatorio generado y el valor mapeado al intervalo [a, b].
        """
        result = []  # Inicializa una lista vacía para almacenar los resultados

        for _ in range(self.num_iterations):  # Itera el número de veces especificado
            seed_squared = str(self.seed ** 2).zfill(2 * self.n_digits)  # Calcula el cuadrado de la semilla y lo rellena con ceros a la izquierda

            start = (len(seed_squared) - self.n_digits) // 2  # Calcula el índice de inicio para extraer los dígitos del medio
            new_seed = int(seed_squared[start:start + self.n_digits])  # Extrae los dígitos del medio y los convierte a entero

            random_num = new_seed / (10 ** self.n_digits)  # Normaliza el número aleatorio al intervalo [0, 1)

            mapped_value = self.a + (self.b - self.a) * random_num  # Mapea el número aleatorio al intervalo [a, b]

            result.append([round(self.seed, 5), round(random_num, 5), round(mapped_value, 5)])  # Agrega la semilla, el número aleatorio y el valor mapeado a la lista de resultados

            self.seed = new_seed  # Actualiza la semilla para la siguiente iteración

        return result  # Devuelve la lista de resultados