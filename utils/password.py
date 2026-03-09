from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def secure_password(raw_password):
    hashed = password_context.hash(raw_password)
    return hashed

def verify_password(plain, hash):
    return password_context.verify(plain, hash)
