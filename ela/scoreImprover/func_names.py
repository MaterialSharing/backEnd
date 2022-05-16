import inspect

from cxxulib.printer import print1

v1 = 123
v2 = "aa"
argv1 = 'value1'
argv2 = 'value2'
# get parameter names
#通过inspect.signature()方法来获取形参
def foo(a, b, c):
    sig = inspect.signature(foo)
    # print(a, b, c)
    print("@sig:",sig)
    return sig


foo(argv1, argv2, argv2)

# local()方法来获取
def func(a, b):
    keys = locals().keys()
    print(keys)
    parameters=[key for key in keys]
    print("@parameters:",parameters)
    return parameters


func(v1, v2)
# print(func(v1, v2))
# 通过func.__code__属性获取
# print(func.__code__.co_varnames)
# print(func.__code__.co_)

#获取传入的实参(不可靠的方法)
# 在函数外部获取变量信息
loc = locals()


# def locals() -> dict[str, Any]
# Return a dictionary containing the current scope's local variables.
# NOTE: Whether or not updates to this dictionary will affect name lookups in the local scope and vice-versa is implementation dependent and not covered by any backwards compatibility guarantees.
def get_argvs(value1, value2):
    # print(loc)
    # print1(locals(),is_dict=1)
    # print(type(loc))
    # print1(loc,is_dict=1)
    # print(loc.keys())
    # print(loc.get("loc"))
    # print(type(loc.get("loc"))
    # print1(loc.get("loc"), is_dict=1)
    # print(loc["bbb"])
    # vars=loc.pop("loc")
    # del loc["loc"]
    # print(loc)
    # print1(vars,is_dict=1)
    # print("@type:",type(loc))
    argvs = []
    # values = inspect.signature(get_argvs)
    values = [value1, value2]
    for key in loc:
        if loc[key] in values:
            argvs.append(key)
            print("argvName:", key, ":", loc[key])
    print("done!")
    return argvs


print(get_argvs(argv1, argv2))



