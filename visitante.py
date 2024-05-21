class Grafo:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def exportar_a_xml(self, visitor):
        for nodo in self.nodos:
            nodo.accept(visitor)


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre

    def accept(self, visitor):
        raise NotImplementedError


class Ciudad(Nodo):
    def __init__(self, nombre, latitud, longitud, poblacion):
        super().__init__(nombre)
        self.latitud = latitud
        self.longitud = longitud
        self.poblacion = poblacion

    def accept(self, visitor):
        visitor.visit_ciudad(self)


class Industria(Nodo):
    def __init__(self, nombre, sector, empleados):
        super().__init__(nombre)
        self.sector = sector
        self.empleados = empleados

    def accept(self, visitor):
        visitor.visit_industria(self)


class LugarTurismo(Nodo):
    def __init__(self, nombre, tipo, descripcion):
        super().__init__(nombre)
        self.tipo = tipo
        self.descripcion = descripcion

    def accept(self, visitor):
        visitor.visit_lugar_turismo(self)


class ExportarXMLVisitor:
    def __init__(self):
        self.xml = ""

    def visit_ciudad(self, ciudad):
        self.xml += f"<ciudad nombre=\"{ciudad.nombre}\">\n"
        self.xml += f"\t<ubicacion latitud=\"{ciudad.latitud}\" longitud=\"{ciudad.longitud}\"/>\n"
        self.xml += f"\t<poblacion>{ciudad.poblacion}</poblacion>\n"
        self.xml += "</ciudad>\n"

    def visit_industria(self, industria):
        self.xml += f"<industria nombre=\"{industria.nombre}\">\n"
        self.xml += f"\t<sector>{industria.sector}</sector>\n"
        self.xml += f"\t<empleados>{industria.empleados}</empleados>\n"
        self.xml += "</industria>\n"

    def visit_lugar_turismo(self, lugar_turismo):
        self.xml += f"<lugarTurismo nombre=\"{lugar_turismo.nombre}\">\n"
        self.xml += f"\t<tipo>{lugar_turismo.tipo}</tipo>\n"
        self.xml += f"\t<descripcion>{lugar_turismo.descripcion}</descripcion>\n"
        self.xml += "</lugarTurismo>\n"

    def get_xml(self):
        return self.xml


def crear_grafo():
    grafo = Grafo()

    ciudad1 = Ciudad("Medellín", 6.24, -75.57, 2.500000)
    ciudad2 = Ciudad("Bogotá", 4.61, -74.07, 7.973000)
    industria1 = Industria("Industria textil Antioquia", "Textil", 10.000)
    industria2 = Industria("Acerías Paz del Río", "Metalurgia", 5.000)
    lugar_turismo1 = LugarTurismo("Parque Lleras", "Parque urbano", "Un lugar para disfrutar del aire libre y la vida nocturna")
    lugar_turismo2 = LugarTurismo("Museo de Antioquia", "Museo de arte", "Exhibe obras de arte colombiano e internacional")

    grafo.agregar_nodo(ciudad1)
    grafo.agregar_nodo(ciudad2)
    grafo.agregar_nodo(industria1)
    grafo.agregar_nodo(industria2)
    grafo.agregar_nodo(lugar_turismo1)
    grafo.agregar_nodo(lugar_turismo2)

    return grafo


if __name__ == "__main__":
    grafo = crear_grafo()
    visitor = ExportarXMLVisitor()
    grafo.exportar_a_xml(visitor)

    xml = visitor.get_xml()
    print(xml)
