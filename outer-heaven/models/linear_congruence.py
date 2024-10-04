class LinearCongruence:
    """
    Genera números pseudoaleatorios utilizando el método de Congruencia Lineal.

    Args:
        xo (int): Valor inicial (semilla).
        n (int): Número de iteraciones (cantidad de números a generar).
        k (int): Parámetro k en la fórmula de congruencia lineal.
        c (int): Parámetro c en la fórmula de congruencia lineal.
        g (int): Parámetro g en la fórmula de congruencia lineal.
        min_val (float): Límite inferior del intervalo de mapeo.
        max_val (float): Límite superior del intervalo de mapeo.

    Methods:
        generate(): Genera una lista de números pseudoaleatorios.
    """

    def __init__(self, xo, n, k, c, g, min_val, max_val):
        """
        Inicializa la clase LinearCongruence.

        Args:
            xo (int): Valor inicial.
            n (int): Número de iteraciones.
            k (int): Parámetro k.
            c (int): Parámetro c.
            g (int): Parámetro g.
            min_val (float): Límite inferior del intervalo.
            max_val (float): Límite superior del intervalo.
        """
        self.xo = xo  # Almacena el valor inicial
        self.n = n  # Almacena el número de iteraciones
        self.k = k  # Almacena el parámetro k
        self.c = c  # Almacena el parámetro c
        self.g = g  # Almacena el parámetro g
        self.min_val = min_val  # Almacena el límite inferior del intervalo
        self.max_val = max_val  # Almacena el límite superior del intervalo

    def generate(self):
        """
        Genera una lista de números pseudoaleatorios utilizando el método de Congruencia Lineal.

        Returns:
            list: Una lista de listas, donde cada sublista contiene el valor de xi, el número aleatorio generado (Ri) y el valor mapeado al intervalo [min_val, max_val] (Ni).
        """
        a = 1 + 2 * self.k  # Calcula el valor de 'a'
        m = 2 ** self.g  # Calcula el valor de 'm'
        results = []  # Inicializa una lista vacía para almacenar los resultados
        xi = self.xo  # Inicializa xi con el valor inicial

        for _ in range(self.n):  # Itera el número de veces especificado
            xi = (a * xi + self.c) % m  # Aplica la fórmula de congruencia lineal para calcular el siguiente xi
            Ri = xi / (m - 1)  # Normaliza xi al intervalo [0, 1)
            Ni = self.min_val + Ri * (self.max_val - self.min_val)  # Mapea Ri al intervalo [min_val, max_val]
            results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])  # Agrega los valores a la lista de resultados

        return results  # Devuelve la lista de resultados
