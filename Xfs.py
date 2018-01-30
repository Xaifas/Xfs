# def command(cmd):
#     def add_attribute(func):
#         if not hasattr(func, "command"):
#             func.command = []
#         func.command.append(cmd)
#         return func
#     return add_attribute
#
# @command("qq")
# @command("test")
# def test(x, y):
#     print(x + y)
#
#
#
# if hasattr(test, "command"):
#     print(test.command)