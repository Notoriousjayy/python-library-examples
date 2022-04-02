import os.path

"""
It is possible to work with paths that include "variable" components
that can be expanded automatically.

For example expanduser() converts the tilde (~) character to the name
of a user's home directory.

If the user's home directory cannot be found, the string is returned
unchanged, as with ~nosuchuser in this example.
"""
for user in ['', "jordan", "nosuchuser"]:
    lookup = '~' + user
    print("{!r:>15} : {!r}".format( lookup, os.path.expanduser(lookup)))