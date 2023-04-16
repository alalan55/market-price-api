from typing import Optional


def success_response_dto(status: Optional[int] = None, content: Optional[dict or list] = None, message: Optional[str] = None):
    return {
        "status": status,
        "content": content,
        "message": message
    }


def not_found_item_dto(message: str, content: Optional[dict or list or str] = None):
    return {
        "status": 404,
        "content": content,
        "message": message
    }
