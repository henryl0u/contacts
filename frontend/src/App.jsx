import { useState, useEffect } from "react";
import ContactList from "./components/ContactList";
import ContactForm from "./components/ContactForm";
import "./App.css";

function App() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
      const url = "http://127.0.0.1:5000/contacts"
      const response = await fetch(url);
      const data = await response.json();
      setContacts(data.contacts);
      console.log(data.contacts);
  };

  return (
    <>
    <ContactList contacts={contacts} />
    <ContactForm />
    </>
  )
  
}

export default App;
