import re

def _dashCapitalize(name):
    """
    Return a byte string which is capitalized using '-' as a word separator.

    @param name: The name of the header to capitalize.
    @type name: C{bytes}

    @return: The given header capitalized using '-' as a word separator.
    @rtype: C{bytes}
    """
    if not isinstance(name,bytes):
        name = bytes(name,encoding='utf8')
    return b'-'.join([word.capitalize() for word in name.split(b'-')])

print(_dashCapitalize("ni-hao"))

a = "abc120"
b = 123
print(a > str(b))