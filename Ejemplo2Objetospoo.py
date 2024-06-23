class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Precio: {self.precio}")
