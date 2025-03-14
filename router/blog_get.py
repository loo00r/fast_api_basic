from router.blog_post import required_functionality
from fastapi import APIRouter
from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# @app.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All blogs provided"}

@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This api retrieving all the blogs',
    response_description='List of available blogs'
    )
def get_all_blogs(page=1, page_size: Optional[int] = None,
                  required_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}",
            "required_parameter": required_parameter}

@router.get('/{id}/comments/{comment_id}', tags=['Comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    """
    return {"message":
            f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f"Blog type: {type.value}"}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id: {id}"}
