from flask_restx import Api

def configure_swagger(app):

    api = Api(
        app,
        version='1.0',
        title='User Management API',
        description='A RESTful API for managing users',
        doc='/swagger'  # Swagger UI URL: http://127.0.0.1:5000/swagger
    )
    return api