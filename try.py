import typing

def fxn(var1)-> typing.List[int]:
    var1 : typing.LiteralString 
    # var1 = "hello"
    # var1 = 25
    return var1

print(type(fxn(25)), fxn(25))


from ctypes import CDLL
lib = CDLL('./example.so')
lib.hello_from_c()


# def getter_setter_gen(name, type_):
#     def getter(self):
#         return getattr(self, "__" + name)

#     def setter(self, value):
#         if not isinstance(value, type_):
#             raise TypeError(f"{name} attribute must be set to an instance of {type_}")
#         setattr(self, "__" + name, value)

#     return property(getter, setter)

# def auto_attr_check(cls):
#     new_dct = {}
#     for key, value in cls.__dict__.items():
#         if isinstance(value, type):
#             value = getter_setter_gen(key, value)
#         new_dct[key] = value

#     # Creates a new class, using the modified dictionary as the class dict:
#     return type(cls)(cls.__name__, cls.__bases__, new_dct)

# # Usage:
# @auto_attr_check
# class MyClass:
#     age: int
#     name: str

# obj = MyClass()
# obj.age = 30  # Valid
# obj.name = "Alice"  # Valid
# obj.age = "thirty"  # Raises TypeError
