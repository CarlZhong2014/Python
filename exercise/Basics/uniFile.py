'''
Example:
    Writes a Unicode string to a file in utf-8 and read it bake in.
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'


hello_out = u'Hello python\n'  # hello_out is a Unicode string.
# bytes_out is a Unicode string after encode in utf-8.
bytes_out = hello_out.encode(CODEC)
f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE, "r")
bytes_in = f.read()
f.close()
# hello_in is a Unicode string after utf-8 decode.
hello_in = bytes_in.decode(CODEC)
print hello_in
