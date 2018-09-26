from app import db

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	city = db.Column(db.String(2), index=True, unique=False)


	def __repr__(self):
		return '<Customer {}>'.format(self.name)
