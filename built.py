class Built:

    def __init__(self, medidor, direccion=None, cliente=None,
                 electro_dependiente=None, registro=None):

        self.medidor = medidor
        self.cliente = cliente
        self.electro_dependiente = electro_dependiente
        self.direccion = direccion


class Casa(Built):

    def __init__(self, medidor, direccion, cliente, electro_dependiente=False):

        Built.__init__(medidor, direccion, cliente, electro_dependiente)


class Edificio(Built):

    def __init__(self, medidor, direccion, nombre, registro):

        Built.__init__(medidor, direccion, None, None, registro)
        self.nombre = nombre


class Departamento(Built):

    def __init__(self, medidor, numero, cliente, electro_dependiente=False):

        Built.__init__(medidor, None, cliente, electro_dependiente)
        self.numero = numero
