
defaults = dict(
    PUBLIC_RELAY_BIND_HOST = '0.0.0.0',
    PUBLIC_RELAY_BIND_PORT = 7110,
    PUBLIC_RELAY_ACCEPT_DOMAINS = [
        "bigsite.example.com", ["127.0.0.1:7221"],
        "littlesite.example.com", ["127.0.0.1:7222"],
        "homesite.example.com", ["127.0.0.1:7223"],
    ]
)

class Void:
    pass


class _Config(object):

    def __init__(self, auto_prefix=None, values=None):
        self._auto_prefix = auto_prefix or ""
        self._values = values or {}

    def _find(self, name):
        found = Void
        name = "%s%s" % (self._auto_prefix, name)
        print("checking %s" % name)
        if name in self._values:
            return self._values[name]
        if name in defaults:
            return defaults[name]
        return found

    def autoprefix(self, name):
        return _Config(name, self._values)

    def require(self, *args):
        for a in args:
            assert self._find(a) is not Void

    def __getattr__(self, name):
        return self._find(name)

config = _Config()
