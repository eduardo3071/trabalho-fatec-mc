from app.data.usuarios_mock import USUARIOS


class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._senha = senha
        self.alterar_nome(nome)

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_perfil(self):
        return type(self).__name__

    def conferir_senha(self, senha):
        return self._senha == senha

    def alterar_nome(self, novo_nome):
        if novo_nome.strip() == '':
            raise ValueError('nome não pode ser vazio')
        self._nome = novo_nome.strip()

    def pode_favoritar(self):
        return True

    def pode_publicar(self):
        return False

    def pode_moderar(self):
        return False

    def __repr__(self):
        return f'{type(self).__name__}({self._nome})'


class Visitante(Usuario):
    pass


class Contribuidor(Usuario):
    def pode_publicar(self):
        return True


class Moderador(Contribuidor):
    def pode_moderar(self):
        return True


PERFIS = {
    'visitante': Visitante,
    'contribuidor': Contribuidor,
    'moderador': Moderador,
}


def carregar_usuarios():
    return [PERFIS[u['perfil']](u['id'], u['nome'], u['senha'])
            for u in USUARIOS]
