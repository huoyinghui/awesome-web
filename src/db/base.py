import os, sys

# sys.path 获取上一级路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_path)


# 项目路径直接导入appConf
from conf import appConf


from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import aiopg


__pool = None
dsn = appConf.db.pg.dsn

async def create_pool(loop, **kwargs):
    global __pool
    __pool = await aiopg.create_pool(
        loop=loop,
        dsn=dsn
    )

# from .actor import Actor
print(appConf.db.pg.url)
engine = create_engine(appConf.db.pg.url, pool_size=20, max_overflow=0, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def main():
    print(Base)

if __name__ == '__main__':
    main()
