from sqlmodel import Field, SQLModel, create_engine
from .model import *

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)