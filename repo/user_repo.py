from sqlalchemy.orm import Session
from models.user import User


class userRepo:

    def __init__(self, db_connection: Session):
        self.db_connection = db_connection

    def get_user_by_email(self, email: str) -> User:
        return self.db_connection.query(User).filter(
            User.email == email,
            User.deleted_at.is_(None)
        ).first()

    def add_user(self, user_data: User) -> User:
        self.db_connection.add(user_data)
        self.db_connection.commit()
        self.db_connection.refresh(user_data)
        return user_data

    def get_user_by_id(self, user_id: str) -> User:
        return self.db_connection.query(User).filter(
            User.id == user_id,
            User.deleted_at.is_(None)
        ).first()

    def update_user(self, user: User) -> User:
        print("user update", user.mfa_enabled,
              user.email, user.mfa_hash, flush=True)
        updated_user: User = self.db_connection.merge(user)
        self.db_connection.commit()
        self.db_connection.refresh(updated_user)
        return updated_user

    def update_last_login(self, user: User) -> User:
        updated_user = self.db_connection.merge(user)
        self.db_connection.commit()
        self.db_connection.refresh(updated_user)
        return updated_user
