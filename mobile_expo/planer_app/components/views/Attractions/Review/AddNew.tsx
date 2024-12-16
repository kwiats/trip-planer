import React from 'react';
import ReviewForm from './AttractionReviewForm';

const AddNewReview: React.FC = () => {
  return <ReviewForm onSubmit={(data) => console.log('Adding review:', data)} />;
};

export default AddNewReview;
