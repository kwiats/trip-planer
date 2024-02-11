import React, { useState } from 'react';
import { View, Text, Image, TouchableOpacity } from 'react-native';
import { attractionTileStyles } from './styles';
import { Attraction, Opinion } from '../../../../Attractions/types';

interface AttractionReviewTileProps {
  attraction: Attraction,
  reviews: Opinion[],
}

const AttractionReviewTile: React.FC<AttractionReviewTileProps> = ({ attraction, reviews }) => {
  const hasImage = attraction.image_url && attraction.image_url.trim() !== '';
  // const [filtersVisible, setFiltersVisible] = useState<boolean>(false);

  return (
    <View style={attractionTileStyles.attractionTile}>
      <View style={attractionTileStyles.attractionContainer}>
        <View style={attractionTileStyles.leftContainer}>
          <View style={attractionTileStyles.imageContainer}>
            {hasImage ? (
              <Image source={{ uri: attraction.image_url }} style={attractionTileStyles.image} />
            ) : (
              <View style={attractionTileStyles.emptyImage} />
            )}
          </View>
          <View style={attractionTileStyles.textContainer}>
            <Text style={attractionTileStyles.title}>{attraction.name}</Text>
            <Text style={attractionTileStyles.category}>{attraction.category}</Text>
            <Text style={attractionTileStyles.description}>{attraction.description}</Text>
          </View>
        </View>
        <View style={attractionTileStyles.rightContainer}>
          <Text style={attractionTileStyles.rate}>{attraction.rating.toFixed(1)}</Text>
          <Text style={attractionTileStyles.reviews}>{reviews.length} reviews</Text>
        </View>
      </View>
      {/* <TouchableOpacity onPress={() => setFiltersVisible(!filtersVisible)}>
        <View style={attractionTileStyles.filtersContainer}>
          <Text style={attractionTileStyles.sortFilterIndicator}>{filtersVisible ? '▲' : '▼'}</Text>
          {filtersVisible ? (<Text style={{ margin: 10 }}>there will be sorting and filters here</Text>) : null}
        </View>
      </TouchableOpacity> */}
    </View>
  );
};

export default AttractionReviewTile;
