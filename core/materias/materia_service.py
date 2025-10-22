from core.materias.materia_repository import MateriaRepository
from core.materias.materia import Materia

class MateriaService:
    def __init__(self):
        self.repository = MateriaRepository()

    def listar_materias(self):
        return self.repository.listar()

    def adicionar_materia(self, materia):
        if isinstance(materia, Materia):
            return self.repository.adicionar(materia)
        else: 
            return None

    def atualizar_materia(self, materia):
        if isinstance(materia, materia):
            if materia.id > 0:
                return self.repository.atualizar(materia)
            else:
                return "ID do materia é obrigatório para a atualização"
        else:
            return None

    def remover_materia(self, materia_id):
        sucesso = self.repositoty.remover(materia_id)
        if not sucesso:
            return None
        else:
            return {"id": materia_id, "removido": True}
        
    def obter_materia_por_id(self, materia_id):
        materia = self.repository.obter_por_id(materia_id)
        if not materia:
            return None
        else:
            return materia