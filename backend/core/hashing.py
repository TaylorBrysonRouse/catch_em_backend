from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hashing - file used to hash password for db storage
class PasswordHasher():
  @staticmethod
  def check_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

  @staticmethod
  def get_password_hash(password):
    return pwd_context.hash(password)