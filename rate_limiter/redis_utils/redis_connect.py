from django.core.cache import cache
import time
import redis
from rest_framework.response import Response
# redis_instance = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
# redis_instance.set("test_key", "test_value")
# cache.set("test_go", "value_golocal")

# print(redis_instance.get("test_key"))
# print(cache.get("test_go"))
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




