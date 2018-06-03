import yaml


class PgConfig(yaml.YAMLObject):
    yaml_tag = u'!PgConfig'

    def __init__(self, dbname, user, password, host, port='5432', pool_size=4, echo=True):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.pool_size = pool_size
        self.echo = echo
        self.url = 'postgresql://{user}:{password}@{host}/{dbname}'.format(
            user=self.user, password=self.password, host=self.host, dbname=self.dbname)
        self.dsn = 'dbname={} user={} password={} host={} port={}'.format(
            self.dbname, self.user, self.password, self.host, self.port
        )

    def reset(self):

        self.url = 'postgresql://{user}:{password}@{host}/{dbname}'.format(
            user=self.user, password=self.password, host=self.host, dbname=self.dbname)
        self.dsn = 'dbname={} user={} password={} host={} port={}'.format(
            self.dbname, self.user, self.password, self.host, self.port
        )
        # print("PgConfig:", self.url, self.dsn)

    def __repr__(self):
        return "%s(dbname=%s, user=%s, password=%s, host=%s port=%s pool=%r echo=%r)" % (
            self.__class__.__name__, self.dbname, self.user,  self.password, self.host, self.port,
            self.pool_size, self.echo
        )


class DbConfig(yaml.YAMLObject):
    yaml_tag = u'!DbConfig'

    def __init__(self, dbname, user, password, host, port='5432', pool_size=4, echo=True):
        self.pg = PgConfig(dbname, user, password, host, port=port, pool_size=pool_size, echo=echo)

    def __repr__(self):
        return "%s(pg=%s)" % (self.__class__.__name__, self.pg)


class AppConfig(yaml.YAMLObject):
    yaml_tag = u'!AppConfig'

    def __init__(self, dbname, user, password, host, port='5432', pool_size=4, echo=True):
        self.db = DbConfig(dbname, user, password, host, port=port, pool_size=pool_size, echo=echo)

    def __repr__(self):
        return "%s(db=%s)" % (self.__class__.__name__, str(self.db))


def create_conf():
    with open('./app_tmp.yaml', 'w') as f:
        yaml.dump(data=AppConfig(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432',
            pool_size=4,
            echo=True,
        ), stream=f, default_flow_style=False)


def load_conf(path='../conf/config.yaml'):
    try:
        with open(path, 'r') as f:
            data = "".join(f.readlines())
            app = yaml.load(data)
            print(app)
            return app
    except Exception as e:
        raise e
        return None


appConf = load_conf()
appConf.db.pg.reset()


def main():
    create_conf()
    # app = load_conf()
    print(appConf.db.pg.url)
    pass


if __name__ == '__main__':
    main()
