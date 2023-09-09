import time
import json
from rate_limiter.settings import redis_instance


class RedisUtils:

    @classmethod
    def get(cls, key_name):
        return redis_instance.get(key_name)

    @classmethod
    def user_count(cls, key_name, update_cnt=False):
        if update_cnt:
            curr_count = cls.get(key_name) or 0
            redis_instance.set(key_name, int(curr_count)+1)

        return redis_instance.get(key_name) or 0

    @classmethod
    def clear(cls, key_name):
        return redis_instance.delete(key_name)

    @classmethod
    def get_and_set_rate_limit(cls, request, max_requests, window_size):
        # Generate a unique identifier for the user or IP address
        # can be customised more
        user_identifier = request.user.username if request.user.is_authenticated else request.META['REMOTE_ADDR']
        # Calculate the start and end timestamps for the sliding window
        end_time = int(time.time())
        start_time = end_time - window_size

        # Retrieve the request history for the user/IP from cache and deserialize it
        request_history = redis_instance.get(user_identifier)
        if request_history is None:
            request_history = []

        # Remove timestamps that are outside the sliding window
        request_history_json = json.loads(request_history)
        request_history = [timestamp for timestamp in request_history_json if timestamp >= start_time]

        # Check if the number of requests within the window exceeds the limit
        if len(request_history) >= max_requests:
            return False  # Rate limit exceeded

        # Add the current request timestamp to the history
        request_history.append(end_time)

        # Serialize the updated request history and save it in cache
        redis_instance.set(user_identifier, json.dumps(request_history))

        return True  # Request allowed




