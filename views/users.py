from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        request_json = request.json
        user = user_service.create(request_json)
        return "", 201, {"location": f"/users/{user.id}"}

@user_ns.route('/<int:rid>')
class UserView(Resource):
    def get(self, rid):
        user = user_service.get_one(rid)
        result = UserSchema.dump(user)
        return result, 200

    def put(self, rid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = rid

        user_service.update(request_json)
        return "", 204

    def delete(self,rid):
        user_service.delete(rid)
        return "", 204