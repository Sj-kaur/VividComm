// src/ContactList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ContactList({ token }) {
  const [contacts, setContacts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchContacts = async () => {
      try {
        const response = await axios.get('/api/users/contacts/', {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        setContacts(response.data);
      } catch (err) {
        setError('Failed to fetch contacts.');
        console.error('API Error:', err.response ? err.response.data : err.message);
      } finally {
        setLoading(false);
      }
    };

    if (token) {
      fetchContacts();
    }
  }, [token]);

  if (loading) {
    return <p>Loading contacts...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="contact-list">
      <h2>Contacts</h2>
      {contacts.length > 0 ? (
        <ul>
          {contacts.map(contact => (
            <li key={contact.id}>
              {contact.username}
            </li>
          ))}
        </ul>
      ) : (
        <p>No other users found.</p>
      )}
    </div>
  );
}

export default ContactList;