import Xfs.module as module


@module.command("test")
def foo(x, y):
    return x + y

