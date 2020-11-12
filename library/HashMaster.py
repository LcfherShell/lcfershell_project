import hashlib
import base64

class Hashing:
    def __init__(self, x, y):
        self.o = x
        self.a = y
    def Hasher(self):
        text =  self.o
        opsi =  self.a
        if opsi == "md5":
            return hashlib.md5(text.encode('utf-8')).hexdigest()
        elif opsi == "sha1":
            return hashlib.sha1(text.encode('utf-8')).hexdigest()
        elif opsi == "sha224":
            return hashlib.sha224(text.encode('utf-8')).hexdigest()
        elif opsi == "sha256":
            return hashlib.sha256(text.encode('utf-8')).hexdigest()
        elif opsi == "sha384":
            return hashlib.sha384(text.encode('utf-8')).hexdigest()
        elif opsi == "sha512":
            return hashlib.sha512(text.encode('utf-8')).hexdigest()
        elif opsi == "base64Decode":
            base64_message = text
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            base64_message = message_bytes.decode('ascii')
            return base64_message
        elif opsi == "base64Encode":
            message = text
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            return base64_message
        return "Error"




print(' * Running Module: HashMaster')

#hashing = Hashing("YW5qaW5n", "base64Decode")
#print(hashing.Hasher())