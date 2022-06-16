import hashlib

print(hashlib.sha1(b'Hello world!').hexdigest())

print(hashlib.sha1(b'sdjkiasbkasjb' + b'Hello world!').hexdigest())

s = hashlib.sha1(b'Hello world!').hexdigest()
print(s.encode('utf-8'))

print(hashlib.sha1(b'sdjkiasbkasjb' + bytes(s.encode('utf-8'))).hexdigest())
