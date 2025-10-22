class Usuario:
    def __init__(self, id=None, usuario="", senha="", ativo=False):
        self.__id = id
        self.__usuario = usuario
        self.__senha = senha
        self.__ativo = ativo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id
    
    @property
    def usuario(self):
        return self.__usuario
    @id.setter
    def usuario(self, novo_usuario):
        self.__usuario = novo_usuario

    @property
    def senha(self):
        return self.__senha
    @id.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
    
    @property
    def ativo(self):
        return self.__ativo
    @id.setter
    def ativo(self, novo_ativo):
        self.__ativo = novo_ativo