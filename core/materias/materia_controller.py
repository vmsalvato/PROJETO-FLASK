from flask import Blueprint, request, jsonify
from core.materia.materia_repository import MateriaRepository
from core.materia.materia import materia
from core.autenticacao.autenticacao import autenticacao

materia_service = MateriaService()

materia_controller = Blueprint('materia', __name__, url_prefix='/materias')

@materia_controller.route('/', methods=['GET'])
@autenticacao
def listar_materias():
    materiaes = materia_service.listar_materias()
    return jsonify(materias)

@materia_controller.route('/', methods=['POST'])
@autenticacao
def adicionar_materia():
    dados = request.get_json()
    obj_materia =  Materia(id=0, nome=dados["nome"], sigla_curricular=dados["sigla_curricular"], descricao=dados["descricao"])
    materia_service.adicionar_materia(obj_materia)
    return jsonify(materia), 201

@materia_controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter_materia(id):
    materia = materia_service.obter_materia_por_id(id)
    if materia:
        return jsonify(materia)
    else:
        return jsonify({"Erro": "materia não encontrado"}), 404

@materia_controller.route('/<int:id>', methods=['DELETE'])
@autenticacao
def remover_materia(id):
    sucesso = materia_service.remover_aluno(id)
    return jsonify(sucesso)

@materia_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_materia():
    dados = request.get_json()
    obj_materia = Materia(id=dados["id"], nome=dados["nome"], sigla_curricular=dados["sigla_curricular"], descricao=dados["descricao"])
    materia = materia_service.atualizar_materia(obj_materia)
    if materia:
        return jsonify(materia)
    else: 
        return jsonify({"Erro": "materia não encontrado"}), 404
