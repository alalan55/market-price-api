from typing import Optional


def success_response_model(status: Optional[int] = None, content: Optional[dict or list] = None, message: Optional[str] = None):
    return