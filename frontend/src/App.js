import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [data, setData] = useState([]);
  const [newData, setNewData] = useState('');

  const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';

  useEffect(() => {
    fetch(`${backendUrl}/`)
      .then(response => response.json())
      .then(data => setMessage(data.message));

    fetchData();
  }, []);

  const fetchData = () => {
    fetch(`${backendUrl}/data`)
      .then(response => response.json())
      .then(data => setData(data));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`${backendUrl}/data`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name: newData })
    })
    .then(response => response.json())
    .then(data => {
      setNewData('');
      fetchData();
    });
  };

  return (
    <div>
      <h1>{message}</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={newData} 
          onChange={(e) => setNewData(e.target.value)} 
          placeholder="Enter new data" 
        />
        <button type="submit">Add Data</button>
      </form>
      <ul>
        {data.map((item, index) => (
          <li key={index}>{item[1]}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
