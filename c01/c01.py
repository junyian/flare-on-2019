bytes = "\x03 &$-\x1e\x02 //./"

o = ""
for c in bytes:
    o += chr(ord(c) ^ ord('A'))
print(o)