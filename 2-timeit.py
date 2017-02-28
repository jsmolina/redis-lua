from luaredis import LuaRedisClient
from helpers import NoLuaRedis
import timeit


if __name__ == "__main__":
    lr = LuaRedisClient()

    lr.load_lua_script('./helpers.lua')

    lr.preload()
    print("sum of keys?")
    print(lr.sum_keys())
    print("how much time to execute registering script in redis lua?")
    print(timeit.Timer(lambda: lr.sum_keys()).timeit(number=200))

    nl = NoLuaRedis()

    nl.preload()
    print("\nsum of keys?")
    print(nl.sum_keys())
    print("how much time to execute it in some redis commands?")
    print(timeit.Timer(lambda: nl.sum_keys()).timeit(number=200))
