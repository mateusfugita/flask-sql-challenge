from app import db

class AddressState(db.Model):
    __tablename__ = 'address_states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    uf = db.Column(db.String, nullable=True)
    address_cities = db.relationship("AddressCity", backref='address_state')
