import hashlib,base64

class Encrypt(object):

    def __init__(self):
        pass

    def encrypt_md5(self,string):
        
        return hashlib.md5(string).hexdigest()

    def encrypt_sha1(self,string):

        return hashlib.sha1(string).hexdigest()

    def encrypt_sha224(self,string):
        
        return hashlib.sha224(string).hexdigest()
    
    def encrypt_sha256(self,string):
        
        return hashlib.sha256(string).hexdigest()
    
    def encrypt_sha384(self,string):
        
        return hashlib.sha384(string).hexdigest()

    def encrypt_sha512(self,string):
        
        return hashlib.sha512(string).hexdigest()

    def encode_b64(self,string):

        return  base64.b64encode(string)

    def decode_b64(self,string):
        
        return  base64.b64decode(string)
