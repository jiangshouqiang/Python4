class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        print('name = ',name)
        for k,v in attrs.items():
            print("k = ",k)
            print("v = ",v)
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        print(**kw)
        super(Model,self).__init__(**kw)

class User(Model):
    def __init__(self,name,age):
        self._name = name
        self._age = age

user = User(name='jiang',age=12)

class ListMetaclass(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value : self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

L = MyList()
L.add(12)
L.add(2)
L.add(122)
print(L)