
def print1(prompt_str="",iterable="the iterable",is_dict=0):
    cnt=0
    print(prompt_str,end="")
    if(is_dict):
        iterable=iterable.items()
        # for item in iterable.items():
            # print(item)
        # for key,value in iterable.items():
        #     print(key,value)
    for item in iterable:
        cnt+=1
        # @itemtype={type(item)}
        print(f"@cnt={cnt};@item={item}")

# d={"a":1,"b":2}
# iterable=d.items()
# # for key,value in iterable.items():
# #     print(key,value)
# # for item in iterable:
# #     print
# print1(d,is_dict=1)