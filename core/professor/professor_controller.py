from flask import Blueprint, request, jsonify
from core.professor.professor_repository import ProfessorRepository
from core.professor.professor import Professor
from core.autenticacao.autenticacao import autenticacao

professor_service = ProfessorService()

professor_controller = Blueprint('professor', __name__, url_prefix='/professores')

@professor_controller.route('/', methods=['GET'])
@autenticacao
def listar_professores():
    professores = professor_service.listar_professores()
    return jsonify(professores)

@professor_controller.route('/', methods=['POST'])
@autenticacao
def adicionar_professor():
    dados = request.get_json()
    obj_professor =  Professor(id=0, nome=dados["nome"], idade=dados["idade"], formacao=dados["formacao"])
    professor_service.adicionar_professor(obj_professor)
    return jsonify(professor), 201

@professor_controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter_professor(id):
    professor = professor_service.obter_professor_por_id(id)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"Erro": "Professor não encontrado"}), 404

@professor_controller.route('/<int:id>', methods=['DELETE'])
@autenticacao
def remover_professor(id):
    sucesso = professor_service.remover_aluno(id)
    return jsonify(sucesso)

@professor_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_professor():
    dados = request.get_json()
    obj_professor = Professor(id=dados["id"], nome=dados["nome"], idade=dados["idade"], formacao=dados["formacao"])
    professor = professor_service.atualizar_professor(obj_professor)
    if professor:
        return jsonify(professor)
    else: 
        return jsonify({"Erro": "Professor não encontrado"}), 404
