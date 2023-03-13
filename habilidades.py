from flask_restful import Resource

habilidades = ["Python", "Flask", "JavaScipt", "SQL", "GIT"]

class Habilidades(Resource):
    def get(self):
        return habilidades