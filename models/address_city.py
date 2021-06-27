from app import db

class AddressCity(db.Model):
    __tablename__ = 'address_cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    address_state_id = db.Column(db.Integer, db.ForeignKey('address_states.id'), nullable=True)
    buyers = db.relationship("Buyer", backref='address_city')
