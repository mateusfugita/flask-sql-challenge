import models.buyer as buy
import models.address_city as city
import models.address_state as state
from app import db

Buyer = buy.Buyer
AddressCity = city.AddressCity
AddressState = state.AddressState

def create(data):
    try:
        buyer = buy.Buyer(first_name=data['first_name'], 
                last_name=data['last_name'],
                document=data['document'], 
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                address_city_id=data['address_city_id'])
        db.session.add(buyer)
        db.session.commit()
        return { 'status': 200, 'message': 'Criado com sucesso' }
    except Exception as e:
        print(e)
        return { 'status': 400, 'message': 'Erro na requisição' }

def selectOne(id: int):
    try:
        result = db.session.query(Buyer.first_name, Buyer.last_name, Buyer.email, Buyer.address, AddressCity.name, AddressState.uf) \
                .join(AddressCity, Buyer.address_city_id == AddressCity.id).join(AddressState, AddressCity.address_state_id == AddressState.id).filter(Buyer.id == id).first()

        if result == None:
            return { 'status': 200, 'message': 'Nenhum resultado encontrado' }
        
        response = {
            'status': 200,
            'full_name': result[0] + ' ' + result[1],
            'email': result[2],
            'address': result[3] + ' - ' + result[4] + '/' + result[5]
        }
        return response
    except Exception as e:
        print(e)
        return { 'status': 400, 'message': 'Erro na requisição' }
