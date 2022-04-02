import pathlib

"""
To instantiate a new ath, give a string as the first argument. The
string representation of the path object is the name value. To create
a new path referring to a value relative to an existing path, use the
/ operator to extend the path. The argument to the operator can
either be a string or another path object.

As the value for root in this example shows, the operator combines
the path values as they are given, and does not normalize the
result when it contains the parent reference "..". If a segment
begins with the path separator, however, it is interpreted as a new
"root" reference in the same way as os.path.join(). Extra path
separators are removed from the middle of the path value.
"""

user = pathlib.PurePosixPath("/Users")
print(user)

user_local = user / "w59842"
print(user_local)

user_share = user / pathlib.PurePosixPath("Public")
print(user_share)

root = user / ".."
print(root)

etc = root / "Administer"
print(etc)