import React from "react";

const ContactList = ({ contacts, updateContact, updateCallback }) => {
  const onDelete = async (id) => {
    try {
      const url = `http://127.0.0.1:5000/delete_contact/${id}`;
      const options = {
        method: "DELETE",
      };
      const response = await fetch(url, options);
      if (response.status === 200) {
        updateCallback();
      } else {
        const data = await response.json();
        alert(data.message);
      }
    } catch (error) {
      console.error("An error occurred", error);
    }
  };

  return (
    contacts.length === 0 ? <h1>No contacts found</h1> :
    <div>
      <h1>Contacts</h1>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone Number</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
              <td>{contact.firstName}</td>
              <td>{contact.lastName}</td>
              <td>{contact.email}</td>
              <td>{contact.phoneNumber}</td>
              <td>
                <button onClick={() => updateContact(contact)}>Edit</button>
                <button onClick={() => onDelete(contact.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ContactList;
