class Produto:

    def __init__(self, codigo: int, valor: float, descricao: str) -> None:
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

    def get_codigo(self) -> None:
        return self.__codigo

    def set_codigo(self, codigo) -> None:
        self.__codigo = codigo

    def get_valor(self) -> None:
        return self.__valor
    
    def set_valor(self, valor) -> None:
        self.__valor = valor

    def get_descricao(self) -> None:
        return self.__descricao

    def set_descricao(self, descricao) -> None:
        self.__descricao = descricao