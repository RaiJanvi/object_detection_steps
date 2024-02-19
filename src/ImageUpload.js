import React, { useState } from 'react';

function ImageUpload() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    //setFile(URL.createObjectURL(e.target.files[0]));
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Failed to upload file');
      }

      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <h2>image prediction</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Predict</button>
      {prediction && <div>Prediction: {prediction}</div>}
    </div>
  );
}

export default ImageUpload;
