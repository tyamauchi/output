import uuid
from sqlalchemy import Column, String, create_engine
from sqlalchemy.dialects.postgresql import UUID  # PostgreSQL用のUUID型
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ORM用のベースクラス
Base = declarative_base()

# テーブルをマッピングするクラス
class User(Base):
    __tablename__ = 'users'

    # 代理識別子（UUID）
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

# データベース接続 (SQLiteを使用)
engine = create_engine('sqlite:///example.db')  # PostgreSQLの場合は 'postgresql://user:password@localhost/dbname'
Base.metadata.create_all(engine)

# セッション作成
Session = sessionmaker(bind=engine)
session = Session()

# 新しいユーザーの作成
new_user = User(name="Alice", email="alice@example.com")
session.add(new_user)
session.commit()

# データの取得
user = session.query(User).filter_by(name="Alice").first()
print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
