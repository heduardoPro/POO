import datetime

class Postagem:
    
    def __init__(self, id: int, titulo: str, texto: str, ano, mes, dia, blog, usuario) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__texto = texto
        self.__data_publicacao = datetime.datetime(ano, mes, dia)
        self.__blog = blog
        self.__usuario = usuario

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, other: int) -> None:
        self.__id = other

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, other: str) -> None:
        self.__titulo = other

    @property
    def texto(self) -> str:
        return self.__texto

    @texto.setter
    def texto(self, other: str) -> None:
        self.__texto = other

    @property
    def data_publicacao(self) -> datetime:
        return self.__data_publicacao

    @data_publicacao.setter
    def data_publicacao(self, other: datetime) -> None:
        self.__data_publicacao = other

    @property
    def blog(self) -> str:
        return self.__blog
    
    @blog.setter
    def blog(self, other: str) -> None:
        self.__blog = other

    @property
    def usuario(self) -> int:
        return self.__usuario

    @usuario.setter
    def usuario(self, other: str) -> None:
        self.__usuario = other
    
    def __str__(self) -> str:
        return '\nID: {} \nTITULO: {} \nTEXTO: {} \nDATA DA PUBLICAÇÃO {} '.format(self.id, self.titulo, self.texto, self.data_publicacao)