class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Dict object')

    def __setattr__(self, key, value):
        self[key] = value

