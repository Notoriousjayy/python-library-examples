import os.path

"""
If any arguments to join begins with os.sep, all of the previous
arguments are discarded and the new ones becomes the beginning of the
return value.
"""

PATHS = [
    ("one", "two", "three"),
    ('/', "one", "two", "three"),
    ("/one", "/two", "/three"),
]

for parts in PATHS:
    print("{} : {!r}".format(parts, os.path.join(*parts)))