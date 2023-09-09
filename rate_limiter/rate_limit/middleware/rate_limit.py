from django.http import HttpResponse

from django.utils.deprecation import MiddlewareMixin
from rate_limiter.settings import MAX_RATE_LIMIT, SLIDING_WINDOW_SIZE
from rate_limiter.redis_utils.redis_connect import RedisUtils


class RateLimitMiddleware(MiddlewareMixin):
    """
    RateLimitMiddleware : limits requests as per config defined in constants.py file.
    """

    def process_request(self, request):
        """
        Custom Middleware for ratelimiter.
        """

        if not RedisUtils.get_and_set_rate_limit(request, MAX_RATE_LIMIT, SLIDING_WINDOW_SIZE):
            return HttpResponse(f"Rate limit exceeded. Please wait for next {SLIDING_WINDOW_SIZE} seconds.", status=429)

        response = self.get_response(request)
        return response
