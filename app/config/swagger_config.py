from flasgger import Swagger

def configure_swagger(app):
    """
    Flasgger üçün Swagger konfiqurasiyası.
    """
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "User Management API",
            "description": "A RESTful API for managing users",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/api/users",
        "schemes": ["http"],
    })
