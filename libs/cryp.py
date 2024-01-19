
from hashlib import sha256

def encode_user_passwd(username, password) -> str:
    return sha256(':'.join([username, password]).encode('UTF-8')).hexdigest()

def encode_generic(q) -> str:
    return sha256(q.encode('UTF-8')).hexdigest()
