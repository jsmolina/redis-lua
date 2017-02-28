from redis import Redis


class LuaRedisClient(Redis):

    def __init__(self, *args, **kwargs):
        super(LuaRedisClient, self).__init__(*args, **kwargs)

    def load_lua_script(self, lua_file):
        for name, snippet in self._get_lua_funcs(lua_file):
            self._create_lua_method(name, snippet)

    def _get_lua_funcs(self, lua_file):
        """
        Returns the name / code snippet pair for each Lua function
        in the atoms.lua file.
        """
        with open(lua_file, "r") as f:
            for func in f.read().strip().split("local function "):
                if func:
                    bits = func.split("\n", 1)
                    name = bits[0].split("(")[0].strip()
                    snippet = bits[1].rsplit("end", 1)[0].strip()
                    yield name, snippet

    def _create_lua_method(self, name, snippet):
        """
        Registers the code snippet as a Lua script, and binds the
        script to the client as a method that can be called with
        the same signature as regular client methods, eg with a
        single key arg.
        """
        script = self.register_script(snippet)

        method = lambda *args: script(keys=args)
        setattr(self, name, method)

    def __getattr__(self, name):
        raise NotImplemented()
