from flask import Blueprint
from flask_restplus import Api

from .user_controller import api as ns1
from .auth_controller import api as ns2


blueprint =  Blueprint('api', __name__, url_prefix='')
api = Api(blueprint,
        title='User RestAPI - Swagger',
        version='0.1',
        description='API, SWAGGER with flask \
                \n  고준성',
        doc='/api/doc/'
)

api.add_namespace(ns1, path='/api')
api.add_namespace(ns2, path='/api')
