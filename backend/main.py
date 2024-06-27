from flask import request, jsonify
from config import app, db
from models import Contact

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = [contact.to_json() for contact in contacts]
    return jsonify({'contacts':json_contacts}), 200

@app.route('/create_contact', methods=['POST'])
def create_contact():
    data = request.json

    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone_number = data.get('phoneNumber')

    if not first_name or not last_name or not email or not phone_number:
        return jsonify({'error': 'Please provide all required fields'}), 400
    
    contact = Contact(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)

    try:
        db.session.add(contact)
        db.session.commit()
        return jsonify({'message': 'Contact created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/update_contact/<int:user_id>', methods=['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({'error': 'Contact not found'}), 404
    
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)
    contact.phone_number = data.get('phoneNumber', contact.phone_number)

    try:
        db.session.commit()
        return jsonify({'message': 'Contact updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/delete_contact/<int:user_id>', methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({'error': 'Contact not found'}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted successfully'}), 200
    
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)