import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = ({ onPrediction }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('image', file);
  
    try {
      const response = await axios.post('http://localhost:8000/predict/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      onPrediction(response.data);
    } catch (error) {
      console.error('Error uploading file', error);
    }
  };
  

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileChange} />
      <button type="submit">Predict</button>
    </form>
  );
};

export default UploadForm;
