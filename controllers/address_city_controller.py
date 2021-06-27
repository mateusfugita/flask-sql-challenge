import models.address_city as city
import models.address_state as state
from app import db

AddressCity = city.AddressCity
AddressState = state.AddressState

def create(data):
    if(data['address_state_id'] != None and checkIfAddressStateExists(data['address_state_id']) == False):
        return { 'status': 400, 'message': 'ID do Estado não existe' }
    
    address_city = AddressCity(name=data['name'], address_state_id = data['address_state_id'])
    db.session.add(address_city)
    db.session.commit()
    return { 'status': 200, 'message': 'Criado com sucesso' }

def selectOne(id: int):
    address_city = AddressCity.query.filter_by(id = id).first()

    if(address_city == None):
        return { 'status': 404, 'message': 'Nenhum resultado encontrado' }
    
    return { 
        'status': 200,
        'id': address_city['id'],
        'name': address_city['name'],
        'address_state_id': address_city['address_state_id']
    }

def checkIfAddressStateExists(id):
    address_state = AddressState.query.filter_by(id = id).first()
    return address_state is not None