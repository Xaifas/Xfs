# Coding utf-8
# modules.py - Decorators for functions that can be triggered

def command(cmd):
    """Decorates a function to set a command to trigger it.
    Example:
        @command("foobar")
        This would trigger on lines starting with ".foobar".
    """
    def add_attribute(func):
        if not hasattr(func, "command")
            func.command = []
        func.command.append(cmd)
        return func
    return add_attribute


def event(event):
    """Decorates a function to set an event to trigger it.
    Example:
        @event("PRIVMSG")
        This would trigger on PRIVMSG raw.
    """
    def add_attribute(func):
        if not hasattr(func, "event")
            func.event = []
        func.event.append(event)
        return func
    return add_attribute


def target(target):
    """Decorates a function to set a target to trigger it.
    Example:
        @target("#foobar")
        This would trigger in channel "#foobar".
    """

