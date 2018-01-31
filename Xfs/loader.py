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
    """Gets all triggerable functions from module.

    Returns a list of tuples with name and function.
    """

    command_functions = []
    all_functions = inspect.getmembers(module, inspect.isfunction)
    for func in all_functions:
        if is_triggerable(func[1]):
            command_functions.append((func[0], func[1]))

    return command_functions


def get_func_attributes(func):
    """Gets all the attributes from triggerable functions.

    Returns a tuple with all the attributes inside "func", also "func" has to be a tuple
    with the function name and the function itself, e.g. "('foo', <function foo at 0x0000023DC051A840>)"
    Example:
        print(get_func_attributes(func))
        ('foo', <function foo at 0x0000023DC051A840>, ['bar'], None, ['PRIVMSG'], None, None, None, None, None)

    The order of the tuple has to stay the same all the time.
    """

    func_name = func[0][0]
    func_obj = func[0][1]
    command = getattr(func_obj, "command", False)
    regexp = getattr(func_obj, "regexp", False)
    event = getattr(func_obj, "event", ["PRIVMSG"])
    priv_msg = getattr(func_obj, "privmsg", False)  # this means private message not PRIVMSG raw
    chan = getattr(func_obj, "chan", False)
    nick = getattr(func_obj, "nick", False)
    host = getattr(func_obj, "host", False)
    owner = getattr(func_obj, "owner", False)
    require_thread = getattr(func_obj, "require_owner", False)
    return (func_name, func.obj, command, regexp, event, priv_msg, chan, nick, host, owner, require_thread)


def is_triggerable(func):
    return any(hasattr(func, attr) for attr in ('command', 'regexp'))


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
# b = get_func_from_module(a)
# print(get_func_attributes(b))
# print(b[0][1](3,5))
