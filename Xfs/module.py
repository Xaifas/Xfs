# Coding utf-8
# module.py - Decorators for functions that can be triggered


def command(command_list):
    """Decorates a function to set one or more commands that triggers it.
    Example:
        @command("foo")
        @command("bar")
        This would trigger on lines starting with ".foo" or ".bar".
        Prefix can be changed with @prefix decorator.
    """
    def add_attribute(func):
        if not hasattr(func, "command"):
            func.command = []
        func.command.append(command_list)
        return func
    return add_attribute


def prefix(prefix_list):
    """Decorates a function to set one or more prefixes that triggers it.
    Example:
        @prefix("!")
        This would trigger on commands starting with "!".
    By default all commands have "." as prefix.
    """
    def add_attribute(func):
        if not hasattr(func, "prefix"):
            func.prefix = []
        func.prefix.append(prefix_list)
        return func
    return add_attribute


def event(event_list):
    """Decorates a function to set one or more events in which it can trigger.
    Example:
        @event("PRIVMSG")
        This would trigger only on PRIVMSG raw.
    """
    def add_attribute(func):
        if not hasattr(func, "event"):
            func.event = []
        func.event.append(event_list)
        return func
    return add_attribute


def require_chan(chan_list):
    """Decorates a function to set one or more channels where it can trigger.
    Example:
        @require_chan("#foobar")
        This would trigger in channel "#foobar".
    """
    def add_attribute(func):
        if not hasattr(func, "chan"):
            func.chan = []
        func.chan.append(chan_list)
        return func
    return add_attribute


def require_nick(nick_list):
    """Decorates a function to set one or more nicks that can trigger it.
    Example:
        @require_nick("foobar")
        This would trigger on lines sent by "foobar".
    """
    def add_attribute(func):
        if not hasattr(func, "nick"):
            func.nick = []
        func.nick.append(nick_list)
        return func
    return add_attribute


def require_host(host_list):
    """Decorates a function to set one or more hosts that can trigger it.
    Example:
        @require_host("foo.bar.com")
        This would trigger on lines sent by "*!*@foo.bar.com".
    """
    def add_attribute(func):
        if not hasattr(func, "host"):
            func.host = []
        func.host.append(host_list)
        return func
    return add_attribute


def regexp(regexp_list):
    """Decorates a function to set one or more regex patterns that can trigger it.
    Example:
        @regexp("^foobar$")
        This would trigger when the entire line matches "foobar".
    """
    def add_attribute(func):
        if not hasattr(func, "regexp"):
            func.regexp = []
        func.regexp.append(regexp_list)
        return func
    return add_attribute


def require_owner():
    """Decorates a function so only the owner can trigger it.
    Example:
        @require_owner
    """
    def add_attribute(func):
        if not hasattr(func, "owner"):
            func.owner = True
        return func
    return add_attribute


def require_privmsg():
    """Decorates a function to only be triggerable from a private message.
    Example:
        @require_privmsg
    """
    def add_attribute(func):
        if not hasattr(func, "priv_msg"):
            func.priv_msg = True
        return func
    return add_attribute


def require_thread():
    """Decorates a function so when it's triggered it starts it's own thread.
    Example:
        @require_thread
    """
    def add_attribute(func):
        if not hasattr(func, "require_thread"):
            func.require_thread = True
        return func
    return add_attribute