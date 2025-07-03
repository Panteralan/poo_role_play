"""
Mi primer juego en Python creando personajes, clases y simulando batallas.
Desarrollado para practicar Programación Orientada a Objetos (POO).

Autor: Alan
"""
class Arma:
    """
    Clase que representa un arma.

    Atributos privados:
        _nombre (str): Nombre del arma.
        __poder (int): Daño o puntos de curación del arma.
        __tipo (str): Tipo del arma, pudiendo ser de 'daño' o 'sanación'
    """

    def __init__(self, nombre, poder, tipo):
        self._nombre = nombre
        self.__poder = poder
        self.__tipo = tipo

    @property
    def nombre(self):
        return self._nombre

    @property
    def poder(self):
        return self.__poder

    @property
    def tipo(self):
        return self.__tipo

    def propiedades_arma(self):
        print(f"Nombre del arma: {self._nombre}\n"
              f"Poder: {self.__poder}\n"
              f"Tipo: {self.__tipo}.")


class Personaje:
    def __init__(self, nombre, nivel_personaje, vida_personaje):
        self._nombre = nombre
        self.__nivel_personaje = nivel_personaje
        self.__vida_personaje = vida_personaje
        self.__vida_maxima = vida_personaje
        self._arma = None

    def equipar_arma(self, arma):
        self._arma = arma
        print(f"{self._nombre} se ha equipado con {arma.nombre}.")

    def atacar(self, objetivo):
        if self._arma and self._arma.tipo.lower() == "daño":
            objetivo.recibir_dano(self._arma.poder)
            print(f"{self._nombre} atacó a {objetivo.nombre} con {self._arma.nombre} causando {self._arma.poder} de daño.")
        else:
            print(f"{self._nombre} no tiene un arma de daño equipada para atacar.")

    def curar_aliado(self, objetivo):
        if self._arma and self._arma.tipo.lower() == "sanación":
            objetivo.curar(self._arma.poder)
            print(f"{self._nombre} usó {self._arma.nombre} para curar a {objetivo.nombre} por {self._arma.poder} puntos.")
        else:
            print(f"{self._nombre} no tiene un arma de sanación equipada para curar.")

    def recibir_dano(self, cantidad):
        self.__vida_personaje -= cantidad
        if self.__vida_personaje < 0:
            self.__vida_personaje = 0
        print(f"{self._nombre} recibió {cantidad} de daño. Vida actual: {self.__vida_personaje} HP.")

    def curar(self, cantidad):
        self.__vida_personaje += cantidad
        if self.__vida_personaje > self.__vida_maxima:
            self.__vida_personaje = self.__vida_maxima
        print(f"{self._nombre} se curó {cantidad} puntos. Vida actual: {self.__vida_personaje} HP.")

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida_personaje(self):
        return self.__vida_personaje

    @property
    def nivel_personaje(self):
        return self.__nivel_personaje

    def __str__(self):
        return f"{self._nombre} (Nivel {self.__nivel_personaje}) - Vida: {self.__vida_personaje}/{self.__vida_maxima} HP"


class Enemigo(Personaje):
    """
    Clase que representa a un enemigo en el juego, derivado de Personaje.

    Atributos privados adicionales:
        __tipo (str): Tipo o clase de enemigo.
        __dano (int): Daño que puede infligir.
        __hab_enemigo (str): Nombre de habilidad que posee el enemigo para atacar a los demas personajes.
    """

    def __init__(self, nombre, nivel_personaje, vida_personaje, tipo_enemigo, dano_enemigo, hab_enemigo):
        super().__init__(nombre, nivel_personaje, vida_personaje)
        self.__tipo = tipo_enemigo
        self.__dano = dano_enemigo
        self.__hab_enemigo = hab_enemigo

    def atacar(self, objetivo):
        """Ataca a otro personaje, infligiendo su daño fijo."""
        objetivo.recibir_dano(self.__dano)
        print(f"{self.nombre} ({self.__tipo}) atacó a {objetivo.nombre} causando {self.__dano} de daño.")


class Aliado(Personaje):
    """
    Clase que representa a un aliado del jugador en el juego.

    Atributos adicionales:
        __habilidad_especial (str): Nombre o tipo de habilidad única del aliado.
    """
    def __init__(self, nombre, nivel_personaje, vida_personaje, hab_especial):
        super().__init__(nombre, nivel_personaje, vida_personaje)
        self.__habilidad_especial = hab_especial

    def usar_habilidad(self):
        """Simula el uso de la habilidad especial del aliado."""
        print(f"{self.nombre} usa su habilidad especial: {self.__habilidad_especial}!")

    def curar_aliado(self, objetivo):
        """Usa un arma de tipo 'sanación' para curar a un aliado."""
        if self._arma and self._arma.tipo.lower() == "sanación":
            objetivo.curar(self._arma.poder)
            print(f"{self._nombre} usó {self._arma.nombre} para curar a {objetivo.nombre} por {self._arma.poder} puntos.")
        else:
            print(f"{self._nombre} no tiene un arma de sanación equipada para curar.")

    @property
    def habilidad_especial(self):
        return self.__habilidad_especial


# --- Ejemplo de uso ---
print("="*40)
print("🏹 ARSENAL DISPONIBLE EN EL JUEGO")
print("="*40)
espada = Arma("Espada de las mil verdades", 60, "Daño")
baculo = Arma("Báculo de Ángel", 35, "Sanación")

espada.propiedades_arma()
baculo.propiedades_arma()

print("\n"+"="*40)
print("🛡 CREACIÓN DE PERSONAJES")
print("="*40)
p1 = Personaje("Alan", 1, 150)
a1 = Aliado("Belén", 1, 150, "Sanadora")
e1 = Enemigo("Orco", 1, 80, "Guerrero", 15, "Ataque con espada")

print(p1)
print(a1)
print(e1)

print("\n"+"="*40)
print("⚔ EQUIPANDO ARMAS")
print("="*40)
p1.equipar_arma(espada)
a1.equipar_arma(baculo)

print("\n"+"="*40)
print("🔥 SIMULACIÓN DE BATALLA")
print("="*40)
e1.atacar(p1)
print(p1)
p1.atacar(e1)
print(e1)
a1.curar_aliado(p1)
print(p1)

"""
Decoración
print(f"{'='*10} 🛡 EQUIPO {'='*10}")
Imprime:
========== 🛡 EQUIPO ==========
print("=" * 40)
Imprime:
========================================
print("="*10 + " BATALLA " + "="*10)
Imprime:
========== BATALLA ==========
Los emogis son caracteres Unicode que los obtube del OpenAi
"""