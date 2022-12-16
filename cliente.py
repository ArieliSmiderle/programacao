class Cliente:

    def __init__(self, nome, saldo, limite, titular):
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite
        self.__titular = titular

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @property
    def saldo(self):
        print("chamando @property saldo()")
        return self.__saldo

    @property
    def titular(self):
        print("chamando @property titular()")
        return self.__titular

    @property
    def limite(self):
        print("chamando @property limite()")
        return self.__limite

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome