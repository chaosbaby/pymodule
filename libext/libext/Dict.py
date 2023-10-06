class Dict(dict):

    def __init__(self, kwargs = {}):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__dict__[key] = Dict(value)
            else:
                self.__dict__[key] = value 

    def __getattr__(self, attr):
        return self.__dict__[attr]

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        del self.__dict__[attr]

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)


def test():
    obj = Dict()
# 添加字段
    obj.name = 'John'
    obj.age = 25
    obj.gender = 'Male'

# 打印对象
    print(obj)  # 输出: {'name': 'John', 'age': 25, 'gender': 'Male'}

# 访问字段
    print(obj.name)  # 输出: John
# 修改字段
    obj.age = 30
    print(obj.age)  # 输出: 30

    my_dict = {
        'name': 'jiyikfql',
        'address': {
            'country': 'Country A',
            'city': 'City A',
            'codes': [1, 2, 3]
        },
    }

    obj = Dict(my_dict)
    print(obj)

if __name__ == "__main__":
    test()
