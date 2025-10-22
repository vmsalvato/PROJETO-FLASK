from flask import Flask 
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import controller


app = Flask(__name__)

#registro controlles
app.register_blueprint(aluno_controller)
app.register_blueprint(controller)

if __name__ == "__main__":
    app.run(debug=True)