import models.address_city as city
from app import db

def create(data):
    address_city = city.AddressCity(name=data['name'], address_state_id = data['address_state_id'])
    db.session.add(address_city)
    db.session.commit()
    return { 'status': 200, 'message': 'Criado com sucesso' }
