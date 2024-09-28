# app/routes/blog_routes.py
from flask import Blueprint, request, jsonify
from app.models.blog_post import BlogPost
from app.database import db

blog_bp = Blueprint('blog_bp', __name__)

@blog_bp.route('/blogposts', methods=['GET'])
def get_blog_posts():
    blog_posts = BlogPost.query.all()
    return jsonify([post.title for post in blog_posts])

@blog_bp.route('/blogposts', methods=['POST'])
def create_blog_post():
    data = request.json
    new_blog_post = BlogPost(
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({'message': 'Blog post created successfully'}), 201
