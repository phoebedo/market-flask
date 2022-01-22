from market import db

class User(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30),nullable = False, unique= True)
    email_address = db.Column(db.String(length=80),nullable = False, unique= True)
    password_hash= db.Column(db.String(length=60),nullable = False)
    budget = db.Column(db.Integer(), nullable = False, default=1000)
    items = db.relationship("Item", backref="owned_user", lazy = True)

    def __repr__(self) -> str:
        return f"username: {self.username}"
class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30),nullable = False, unique= True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(), nullable = False, unique= True)
    description = db.Column(db.String(length=1400))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"Item: {self.name}"