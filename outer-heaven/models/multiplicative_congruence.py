class MultiplicativeCongruence:
    """
    Genera números pseudoaleatorios utilizando el método de Congruencia Multiplicativa.

    Args:
        xo (int): Valor inicial (semilla).
        n (int): Número de iteraciones (cantidad de números a generar).
        t (int): Parámetro t en la fórmula de congruencia multiplicativa.
        g (int): Parámetro g en la fórmula de congruencia multiplicativa.
        min_val (float): Límite inferior del intervalo de mapeo.
        max_val (float): Límite superior del intervalo de mapeo.

    Methods:
        generate(): Genera una lista de números pseudoaleatorios.
    """

    def __init__(self, xo, n, t, g, min_val, max_val):
        """
        Inicializa la clase MultiplicativeCongruence.

        Args:
            xo (int): Valor inicial.
            n (int): Número de iteraciones.
            t (int): Parámetro t.
            g (int): Parámetro g.
            min_val (float): Límite inferior del intervalo.
            max_val (float): Límite superior del intervalo.
        """
        self.xo = xo  # Almacena el valor inicial
        self.n = n  # Almacena el número de iteraciones
        self.t = t  # Almacena el parámetro t
        self.g = g  # Almacena el parámetro g
        self.min_val = min_val  # Almacena el límite inferior del intervalo
        self.max_val = max_val  # Almacena el límite superior del intervalo

    def generate(self):
        """
        Genera una lista de números pseudoaleatorios utilizando el método de Congruencia Multiplicativa.

        Returns:
            list: Una lista de listas, donde cada sublista contiene el valor de xi, el número aleatorio generado (Ri) y el valor mapeado al intervalo [min_val, max_val] (Ni).
        """
        a = 8 * self.t + 3  # Calcula el valor de 'a'
        m = 2 ** self.g  # Calcula el valor de 'm'
        results = []  # Inicializa una lista vacía para almacenar los resultados

        for _ in range(self.n):  # Itera el número de veces especificado
            xi = (a * self.xo) % m  # Aplica la fórmula de congruencia multiplicativa para calcular el siguiente xi
            Ri = xi / (m - 1)  # Normaliza xi al intervalo [0, 1)
            Ni = self.min_val + Ri * (self.max_val - self.min_val)  # Mapea Ri al intervalo [min_val, max_val]
            results.append([round(xi, 5), round(Ri, 5), round(Ni, 5)])  # Agrega los valores a la lista de resultados
            self.xo = xi  # Actualiza el valor de xo para la siguiente iteración

        return results  # Devuelve la lista de resultados
