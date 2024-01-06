from passlib.context import CryptContext

psw_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")