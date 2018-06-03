CREATE TABLE users (
	id SERIAL NOT NULL,
	name VARCHAR,
	email VARCHAR,
	password VARCHAR,
	admin BOOLEAN,
	image VARCHAR,
	created_at DATE,
	PRIMARY KEY (id)
)

INSERT INTO users (name, email, password, admin, image, created_at) VALUES (%(name)s, %(email)s, %(password)s, %(admin)s, %(image)s, %(created_at)s) RETURNING users.id
{'name': 'hyh', 'email': 'hyhlinux@163.com', 'password': 'f8968535d050518010bef66554c11fc1', 'admin': True, 'image': 'http://...', 'created_at': datetime.datetime(2018, 6, 4, 1, 46, 47, 952023)}
