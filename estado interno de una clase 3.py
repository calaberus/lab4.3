class Libro:
    def_init_(self, titulo, autor)
        self. titulo=titulo
        self.autor= autor
        self.disponible= True
    def prestar (self):
        if self.disponible:
            self.disponoble=false 
            print(f"el libro´{self.titulo}´ha sido prestado.")
        else:
            print(f"el libro´{self.titulo}´no esta disponible.")
    def mostar_estado(self):
        estado="disponoble" if self.disponible else "prestado"
        print(f"El Libro´{self.titulo}´esta{estado}.")