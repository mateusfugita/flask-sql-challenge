import models.address_state as state
from app import db

def create(data):
    address_state = state.AddressState(name=data['name'], uf=data['uf'])
    db.session.add(address_state)
    db.session.commit()
    return { 'status': 200, 'message': 'Criado com sucesso' }
