from passlib.context import CryptContext

b_c=CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def decrypt(password:str):
        return b_c.hash(password)
    
    def verify(hashed_password,plain_password):
        return b_c.verify(plain_password,hashed_password)
    
    