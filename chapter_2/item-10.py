# Item 10 - Know the Differences Between bytes and str
print("\n Item 10 - Know the Differences Between bytes and str \n")

print("bytes example - ")
a = b"h\x65llo"
print(type(a))
print(list(a))
print(a)

print("="*30)

print("str example - ")
a = "a\u0300 propos"
print(type(a))
print(list(a))
print(a)

print("="*30)

print("bytes to str - decode")

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of str

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))
print("="*30)

print("str to bytes - encode")

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value  # Instance of bytes

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))

print("="*30)
print("\n Default encoding of the machine - ")
import locale
print(locale.getpreferredencoding())
print("="*30)

print("\n Notes - ")
print("""
** Things to Remember **
bytes contains sequences of 8-bit values, and str contains sequences of Unicode code points.

Use helper functions to ensure that the inputs you operate on are the type of character sequence you expect (8-bit values, UTF-8-encoded strings, Unicode code points, etc).

bytes and str instances can’t be used together with operators (like >, ==, +, and %).

If you want to read or write binary data to/from a file, always open the file using a binary mode (like "rb" or "wb").

If you want to read or write Unicode data to/from a file, be careful about your system’s default text encoding. Explicitly pass the encoding parameter to open to avoid surprises.
""")
print("="*30)