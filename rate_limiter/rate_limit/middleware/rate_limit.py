from django.http import HttpResponsePermanentRedirect, HttpResponse

from django.utils.deprecation import MiddlewareMixin
from rate_limiter.settings import MAX_RATE_LIMIT, SLIDING_WINDOW_SIZE
from rate_limiter.redis_utils.redis_connect import RedisUtils


class RateLimitMiddleware(MiddlewareMixin):
    """
    "Common" middleware for taking care of some basic operations:

        - Forbid access to User-Agents in settings.DISALLOWED_USER_AGENTS

        - URL rewriting: Based on the APPEND_SLASH and PREPEND_WWW settings,
          append missing slashes and/or prepends missing "www."s.

            - If APPEND_SLASH is set and the initial URL doesn't end with a
              slash, and it is not found in urlpatterns, form a new URL by
              appending a slash at the end. If this new URL is found in
              urlpatterns, return an HTTP redirect to this new URL; otherwise
              process the initial URL as usual.

          This behavior can be customized by subclassing CommonMiddleware and
          overriding the response_redirect_class attribute.
    """

    response_redirect_class = HttpResponsePermanentRedirect

    def process_request(self, request):
        """
        Check for denied User-Agents and rewrite the URL based on
        settings.APPEND_SLASH and settings.PREPEND_WWW
        """

        if not RedisUtils.get_and_set_rate_limit(request, MAX_RATE_LIMIT, SLIDING_WINDOW_SIZE):
            return HttpResponse(f"Rate limit exceeded. Please wait for next {SLIDING_WINDOW_SIZE} seconds.", status=429)

        response = self.get_response(request)
        return response
