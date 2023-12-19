import time
from functools import wraps
from fastapi import HTTPException, Request, status
def rate_limited(max_calls: int, time_frame:int):
    def decorator(func):
        """
        Decorator function that enforces rate limiting for an async endpoint.

        Args:
            func (Callable): The function to be decorated.

        Returns:
            Callable: The decorated function that enforces rate limiting.

        Raises:
            HTTPException: If the rate limit is exceeded.

        """
        calls = []
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            now = time.time()
            calls_in_time_frame = [call for call in calls if call > now-time_frame]
            if len(calls_in_time_frame) >= max_calls:
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded")
            calls.append(now)
            return  func(request, *args, **kwargs)
        
        return wrapper
    return decorator