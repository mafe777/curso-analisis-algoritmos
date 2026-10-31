"""Estructuras para gestionar envios."""


class Nodo:
    """Nodo para la lista enlazada."""

    def __init__(self, guia: int, estado: str) -> None:
        self.guia = guia
        self.estado = estado
        self.siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista simplemente enlazada."""

    def __init__(self) -> None:
        self.cabeza: Nodo | None = None
        self.tamano = 0

    def insertar(self, guia: int, estado: str) -> None:
        """Agrega un elemento al inicio."""
        nuevo_nodo = Nodo(guia, estado)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca una guia recorriendo la lista."""
        actual = self.cabeza
        while actual is not None:
            if actual.guia == guia:
                return actual.estado
            actual = actual.siguiente
        return None


class TablaHash:
    """Tabla hash con encadenamiento."""

    def __init__(self, m: int) -> None:
        self.m = m
        self.casillas: list[ListaEnlazada] = [ListaEnlazada() for _ in range(m)]
        self.tamano = 0

    def hash(self, guia: int) -> int:
        """Calcula la posición con modulo."""
        return guia % self.m

    def insertar(self, guia: int, estado: str) -> None:
        """Inserta el envio en la casilla correspondiente."""
        indice = self.hash(guia)
        self.casillas[indice].insertar(guia, estado)
        self.tamano += 1

    def buscar(self, guia: int) -> str | None:
        """Busca el envio en su casilla respectiva."""
        indice = self.hash(guia)
        return self.casillas[indice].buscar(guia)

    def factor_carga(self) -> float:
        """Calcula n / m."""
        return self.tamano / self.m