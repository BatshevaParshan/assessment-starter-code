from flask import Flask, make_response, jsonify 
from config import app, db, api
from models import Project
from flask_restful import Resource, Api

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        if projects:
            projects_data = [project.to_dict()for project in projects]
            return jsonify(projects_data), 200
        else:
            return jsonify({'message': 'No projects found'}), 404
        
class ProjectDel(Resource):
    def delete(self, project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return make_response('',204)
        else:
            return jsonify({'message': 'Project not found'}), 404

api.add_resource(Projects, '/projects')
api.add_resource(ProjectDel, '/projects/<int:project_id>')




    
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)


