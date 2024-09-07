import React, { useState } from 'react';
import Header from '../components/Header';
import UploadForm from '../components/UploadImage';
import PredictionResult from '../components/PredictionResult';

const HomePage = () => {
  const [result, setResult] = useState(null);

  const handlePrediction = (prediction) => {
    setResult(prediction);
  };

  return (
    <div>
      <Header />
      <UploadForm onPrediction={handlePrediction} />
      <PredictionResult result={result} />
    </div>
  );
};

export default HomePage;
