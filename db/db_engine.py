from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy.orm import sessionmaker


# 创建基类
Base = declarative_base()

# 定义 UserInfo 模型
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))
    phone = Column(String(15))


# charset=utf8mb4：设置数据库的字符集为 utf8mb4，支持更广泛的 Unicode 字符
DATABASE_URI = 'mysql+pymysql://root:sonw1234567!@127.0.0.1/langgraph_agent?charset=utf8mb4'   
engine = create_engine(DATABASE_URI, echo=True)

# 如果表不存在，则创建表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()