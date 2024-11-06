from flask import Blueprint, request, jsonify
from app.models.blog_post import BlogPost
from app.database import db
from flask_restx import Api, fields

# Create Blueprint and API instance
blog_bp = Blueprint('blog_bp', __name__)
api = Api(blog_bp)

# Define the BlogPost model for Swagger UI
blog_post_model = api.model('BlogPost', {
    'id': fields.Integer(readonly=True, description='The blog post unique identifier'),
    'title': fields.String(required=True, description='The title of the blog post'),
    'content': fields.String(required=True, description='The content of the blog post'),
    'user_id': fields.Integer(required=True, description='The user who created the post')
})

# GET route: Get all blog posts
@blog_bp.route('/blogposts', methods=['GET'])
def get_blog_posts():
    """
    Get all blog posts
    ---
    tags:
      - Blogs
    responses:
      200:
        description: A list of blog posts
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/models/BlogPost'  # Reference to the model defined in Flask-RESTX
    """
    blog_posts = BlogPost.query.all()
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'user_id': post.user_id
    } for post in blog_posts])

# POST route: Create a new blog post
@blog_bp.route('/blogposts', methods=['POST'])
def create_blog_post():
    """
    Create a new blog post
    ---
    tags:
      - Blogs
    parameters:
      - in: body
        name: blog_post
        description: The blog post to create
        schema:
          $ref: '#/models/BlogPost'  # Correct reference to the model
    responses:
      201:
        description: Blog post created successfully
      400:
        description: Invalid input
    """
    data = request.json
    new_blog_post = BlogPost(
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({'message': 'Blog post created successfully'}), 201