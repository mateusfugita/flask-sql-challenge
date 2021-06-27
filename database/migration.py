import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db
# from models.buyer import Buyer
# from models.address_city import AddressCity
# from models.address_state import AddressState
import models

db.create_all()
