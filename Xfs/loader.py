# Coding = utf-8
# loader.py - Module loader

import os
import importlib.util
import inspect


def load_module(name, path):
    """Load a module from path.
    Example:
        load_module("foobar", "/home/John/foobar.py")
        Loads "foobar" module located in "/home/John/".
    """
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_func_from_module(module):
    """Gets all the functions from module.

    Returns a list of tuples with name and function.
    """
    command_functions = []
    all_functions = inspect.getmembers(module, inspect.isfunction)
    for func in all_functions:
        if hasattr(func[1], "command"):
            command = getattr(func[1], "command")
            event = getattr(func[1], "event")
            target = getattr(func[1], "target")
            nick = getattr(func[1], "nick")
            owner = getattr(func[1], "owner")
            command_functions.append((func[0], func[1], command, event, target, nick, owner))
        # TODO Finish this function

    return command_functions


def check_module(path):
    """Checks if the file from path is a valid module and can be loaded."""
    if os.path.isfile(path) and path.endswith(".py") and not os.path.basename(path).startswith("_"):
        return path
    else:
        return None


def enum_modules():
    """Maps the names of modules to the location of their file.

    Returns a dict mapping the names of modules as keys and their path as values.
    The function only maps modules inside /modules/ folder.
    Example:
        print(enum_modules())
        {'foo': 'path/modules/foo.py', 'bar': 'path/modules/bar.py'}
    """

    modules = {}

    main_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(main_dir, "modules")
    for path in os.listdir(modules_dir):
        module = check_module(os.path.join(modules_dir, path))
        if module is not None:
            modules[path[:-3]] = module
    if modules:
        return modules
    else:
        return None

# a = load_module("test", "modules\\test.py")
# print(get_func_from_module(a))
# for x in get_func_from_module(a):
#     if hasattr(x[1], "t"):
#         print("are")