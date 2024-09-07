import React from 'react';

const PredictionResult = ({ result }) => {
  if (!result) return null;

  return (
    <div>
      <h2>Prediction Result</h2>
      <p>{result.prediction}</p>
    </div>
  );
};

export default PredictionResult;
