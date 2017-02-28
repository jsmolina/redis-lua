import random
from redis import Redis

class NoLuaRedis(object):
    def __init__(self):
        self.redis = Redis()

    def preload(self):
        for i in xrange(1, 100):
            self.redis.set("profile_cache:{0}".format(str(i)), i)

    def sum_keys(self):
        sum = 0
        keys = self.redis.keys('profile_cache:*')
        for key in keys:
            val = self.redis.get(key)
            sum += int(val)
        return sum
