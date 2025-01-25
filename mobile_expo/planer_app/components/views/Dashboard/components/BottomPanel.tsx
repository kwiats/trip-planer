import React, { Dispatch, useEffect, useMemo, useRef } from 'react';
import { Text, TouchableOpacity, View } from 'react-native';
import { Picker } from '@react-native-picker/picker';
import BottomSheet, { BottomSheetScrollView } from '@gorhom/bottom-sheet';
import { styles } from '../styles';
import AttractionTile from '../../common/AttractionTile';
import { Attraction, NavigationProps } from "../../Attraction/types";
import { useNavigation } from "@react-navigation/native";


interface BottomPanelProps {
  isVisible: boolean;
  searchText: string;
  onCategoryChange: (category: string) => void;
  attractions: Attraction[];
  selectedCategory: any;
  headAttractionState: {
    headAttraction: Attraction | undefined,
    setHeadAttraction: Dispatch<React.SetStateAction<Attraction | undefined>>
  },
  onAddToRoute: () => void
}

const getPlaceholderAttractions = () => {
  return Array.from({ length: 8 }, (_, index) => ({
    place_name: `Nazwa Atrakcji ${index + 1}`,
    place_category: `Category ${index + 1}`,
    place_rating: 4.5 + index / 100,
    place_description: `Lorem Ipsum Opis Kwiatuh ${index + 1} Lorem Ipsum Opis Kwiatuh ${
      index + 1
    }Lorem Ipsum Opis Kwiatuh ${index + 1} Lorem Ipsum Opis Kwiatuh ${
      index + 1
    }Lorem Ipsum Opis Kwiatuh ${index + 1}`,
    image_url:
      'https://media.cntraveler.com/photos/58de89946c3567139f9b6cca/16:9/w_1920,c_limit/GettyImages-468366251.jpg',
  }));
};

const BottomPanel: React.FC<BottomPanelProps> = ({
                                                   isVisible,
                                                   searchText,
                                                   onCategoryChange,
                                                   attractions,
                                                   selectedCategory,
                                                   headAttractionState,
                                                   onAddToRoute
                                                 }) => {
  const sheetRef = useRef<BottomSheet>(null);
  const headAttraction = headAttractionState.headAttraction;
  const snapPoints = useMemo(() => {
    return headAttraction ? ['5%', '28%', '80%'] : ['5%', '80%'];
  }, [headAttraction]);
  const placeholderAttractions = useMemo(() => getPlaceholderAttractions(), []);
  const navigation = useNavigation<NavigationProps>();

  useEffect(() => {
    if (headAttraction) {
      sheetRef.current?.snapToIndex(1);
    } else {
      sheetRef.current?.snapToIndex(0);
    }
  }, [headAttraction]);

  return (
    <BottomSheet ref={sheetRef} index={isVisible ? 1 : 0} snapPoints={snapPoints}>
      {headAttraction &&
          <View>
              <AttractionTile
                  attraction={{
                    place_name: headAttraction.name,
                    place_description: headAttraction.description,
                    place_category: headAttraction.category,
                    place_rating: headAttraction.rating.toFixed(1),
                    image_url:
                      'https://media.cntraveler.com/photos/58de89946c3567139f9b6cca/16:9/w_1920,c_limit/GettyImages-468366251.jpg'
                  }}/>
              <View style={styles.buttonContainer}>
                  <TouchableOpacity style={styles.button} onPress={() => onAddToRoute()}>
                      <Text style={styles.buttonText}>Add to Route</Text>
                  </TouchableOpacity>
                  <TouchableOpacity style={styles.button}
                                    onPress={() => navigation.navigate('AttractionDetailScreen', { id: headAttraction?.id })}>
                      <Text style={styles.buttonText}>More Details</Text>
                  </TouchableOpacity>
              </View>
          </View>
      }
      <View style={{ padding: 10 }}>
        <View style={styles.searchSection}>
          <Text>{searchText}</Text>

          <Picker
            style={styles.picker}
            selectedValue={selectedCategory}
            onValueChange={(itemValue) => onCategoryChange(itemValue)}>
            <Picker.Item label="Culture" value="culture"/>
            <Picker.Item label="Food" value="gastronomy"/>
          </Picker>
        </View>
      </View>
      <BottomSheetScrollView>
        <View style={styles.attractionsGrid}>
          {(attractions && attractions.length > 0 ?
              attractions.filter((a) => (a != headAttraction)).map(
                (attraction: Attraction) => (
                  <TouchableOpacity
                    key={attraction.id}
                    onPress={() => {
                    headAttractionState.setHeadAttraction(attraction);
                  }}>
                    <AttractionTile
                      attraction={{
                        place_name: attraction.name,
                        place_description: attraction.description,
                        place_category: attraction.category,
                        place_rating: attraction.rating.toFixed(1),
                        image_url:
                          'https://media.cntraveler.com/photos/58de89946c3567139f9b6cca/16:9/w_1920,c_limit/GettyImages-468366251.jpg'
                      }}
                    />
                  </TouchableOpacity>
                )
              ) : placeholderAttractions.map(
                (attraction, index) => (
                  <AttractionTile key={index} attraction={attraction}/>
                ))
          )}
        </View>
      </BottomSheetScrollView>
    </BottomSheet>
  )
    ;
};

export default BottomPanel;
