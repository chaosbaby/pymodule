class Dict(dict):

    def __init__(self, kwargs = {}):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Dict(value)
            else:
                self.__dict__[key] = value 

    def __getattr__(self, attr):
        if attr not in self.__dict__:
            self.__dict__[attr] = Dict()
        return self.__dict__[attr]

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        
    def __setitem__(self, attr, value):
        self.__dict__[attr] = value

    def __getitem__(self, attr):
        return self.__dict__[attr]

    def __delattr__(self, attr):
        del self.__dict__[attr]

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def to_dict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, Dict):
                dic[key] = value.to_dict()
            else:
                dic[key] = value
        return dic




