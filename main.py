from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/properties")
def get_properties():
    addresses = [
        {"id": 1, "address" : "Morse Close, Harefield, UB9"},
        {"id": 2, "address" : "Dolphin Square, London, SW1V"},
        {"id": 3, "address" : "Warlters Road, Holloway, London, N7"},
        {"id": 4, "address" : "Rockingham Road, Uxbridge"},
        {"id": 5, "address" : "Northwick Avenue, Harrow, HA3"}
    ]

    return addresses

class Property(BaseModel):
    address: str
    price: float
    bedroom: int
    bathroom: int
    reception: int
    size: float

@app.post("/properties")
def create_property(property_data: Property):
    print("Data: ", property_data)
    return{"message" : "Propwrty added successfully", "Property details" : property_data}

#Sample Body
#    {"address": "123 Elm Street, Springfield",
#    "price": 250000.0,
#    "bedroom": 3,
#    "bathroom": 2,
#    "reception": 1,
#    "size": 120.5}


@app.get("/contacts")
def get_contacts():
    contacts = [
        {"id": 1,
         "first_name": "John",
         "last_name": "Amber",
         "phone_number": "+1-111-111-1111",
         "email": "johnamber@blabla.com",
         "address": "Morse Close, Harefield, UB9"},

         {"id": 2,
         "first_name": "Jane",
         "last_name": "Doe",
         "phone_number": "+2-222-222-2222",
         "email": "janedoe@blabla.com",
         "address": "Dolphin Square, London, SW1V"},

        {"id": 3,
         "first_name": "Alice",
         "last_name": "Becker",
         "phone_number": "+3-333-333-3333",
         "email": "alicebecker@blabla.com",
         "address": "Warlters Road, Holloway, London, N7"},

        {"id": 4,
         "first_name": "Bob",
         "last_name": "Green",
         "phone_number": "+4-444-444-4444",
         "email": "bobgreen@blabla.com",
         "address": "Rockingham Road, Uxbridge"},

         {"id": 5,
         "first_name": "Carol",
         "last_name": "Salt",
         "phone_number": "+5-555-555-5555",
         "email": "carolsalt@blabla.com",
         "address": "Northwick Avenue, Harrow, HA3"}
         ]
        
    return contacts

class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str

#We will use this when we want to add new contact in addition to the existing contact details.
@app.post("/contacts")
def create_contact(contact_data: Contact):
    print("Data:", contact_data)
    print("Contact added successfully")
    return {"message": "Contact added successfully", "contact_details": contact_data}
 
# Sample Body 
# {"first_name": "Sila",
#  "last_name": "Azgin",
#  "phone_number": "+6-666-666-6666",
#  "email": "silaazgin@blabla.com",
#  "address": "İstanbul, Sultangazi, Turkiye"}