from services.database_manager import DatabaseManager
import bcrypt

class SimpleHasher:
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))   

class AuthManager:
    """Handles user registration and login."""
    def __init__(self, user_repo=None):
        self.user_repo = DatabaseManager()

    def register_user(self, name, password):
        hash = self.hash_password(password)
        self.user_repo.set_user(name, hash)

    def login_user(self, name, password) -> bool:
        user = self.user_repo.get_one_user(name)
        if user:
            id, name_db, hash = user
            if name == name_db and SimpleHasher().verify_password(hash, password):
                return True
        return False
