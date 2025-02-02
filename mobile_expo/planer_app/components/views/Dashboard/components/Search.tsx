import React from 'react';
import { View, TextInput, TouchableOpacity, Text, Keyboard } from 'react-native';
import { styles } from '../styles';
import { fetchAttractions } from '../api/attractionsApi';
import { fetchLocationFromNominatim } from "../api/nominatimApi";

const Search = ({ setLocation, setAttractions, setSearchText, searchText }: any) => {
  const handleSearch = () => {
    fetchLocationFromNominatim(searchText)
      .then((location) => {
        setLocation(location);
        return fetchAttractions(searchText);
      })
      .then((attractions) => {
         if (attractions && attractions.length > 0) setAttractions(attractions); else console.log('Attraction demo data');
      })
      .catch((error) => {
        // Alert.alert('Error', 'Failed to find location');
        console.error(error);
      });
    Keyboard.dismiss();
  };

  return (
    <View>
      <TextInput
        style={styles.searchInput}
        placeholder="Search for a place"
        value={searchText}
        onChangeText={setSearchText}
      />
      <TouchableOpacity style={styles.searchButton} onPress={handleSearch}>
        <Text>Search</Text>
      </TouchableOpacity>
    </View>
  );
};

export default Search;
