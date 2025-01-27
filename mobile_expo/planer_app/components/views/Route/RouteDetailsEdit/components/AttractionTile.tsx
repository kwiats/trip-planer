import React from 'react';
import { View, Text, Image, TouchableOpacity } from 'react-native';
import { Attraction } from "../../../Attraction/types";
import { attractionTileStyles as styles } from "../../styles";

interface AttractionTileProps {
  attraction: Attraction;
  editeMode: boolean;
  onRemove?: () => void;
}

const AttractionTile: React.FC<AttractionTileProps> = ({ attraction, editeMode, onRemove }) => {
  const hasImage = attraction.image_url && attraction.image_url.trim() !== '';

  return (
    <View style={styles.attractionTile}>
      {editeMode && <Text style={styles.handle}>☰</Text>}
      <View style={styles.leftContainer}>
        <View style={styles.imageContainer}>
          {hasImage ? (
            <Image source={{ uri: attraction.image_url }} style={styles.image} />
          ) : (
            <View style={styles.emptyImage} />
          )}
        </View>
        <View style={styles.textContainer}>
          <Text style={styles.title}>{attraction.name}</Text>
          <View style={styles.subInfoContainer}>
            <Text style={styles.subInfo}>{attraction.country}</Text>
            <Text style={styles.subInfo}> - </Text>
            <Text style={styles.subInfo}>{attraction.city}</Text>
            <Text style={styles.subInfo}> - </Text>
            <Text style={styles.subInfo}>{attraction.category}</Text>
          </View>
        </View>
      </View>
      <Text style={styles.rate}>{attraction.rating}</Text>
      {editeMode &&
          <TouchableOpacity onPress={onRemove}>
              <Text style={styles.remove}>❌</Text>
          </TouchableOpacity>
      }
    </View>
  );
};

export default AttractionTile;
