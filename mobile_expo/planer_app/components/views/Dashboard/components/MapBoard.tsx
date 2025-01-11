import React, { useEffect, useState } from 'react';
import { Alert, Button, ImageURISource, PermissionsAndroid, Platform, View } from 'react-native';
import MapView, { Marker, PROVIDER_DEFAULT, UrlTile } from 'react-native-maps';
import * as Location from 'expo-location';
import { styles } from '../styles';
import Search from './Search';
import BottomPanel from './BottomPanel';
import { fetchAttractions } from '../api/attractionsApi';
import { attractionsExamples } from '../../Attraction/api/fake/apiMock'
import { Attraction } from "../../Attraction/types";

const OsmBoard = () => {
  const [location, setLocation] = useState<boolean>(false);
  const [region, setRegion] = useState({
    latitude: 52.2296756,
    longitude: 21.0122287,
    latitudeDelta: 0.05,
    longitudeDelta: 0.05,
  });
  const [attractions, setAttractions] = useState<Attraction[]>(attractionsExamples);
  const [panelVisible, setPanelVisible] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');

  useEffect(() => {
    if (Platform.OS === 'android') {
      PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION, {
        title: 'Permission to access location',
        message: 'We need your permission to access your location',
        buttonNeutral: 'Ask Me Later',
        buttonNegative: 'Cancel',
        buttonPositive: 'OK',
      }).then((granted) => {
        if (granted === PermissionsAndroid.RESULTS.GRANTED) {
          Location.requestForegroundPermissionsAsync().then((status) => {
            console.log('status', status.status)
            getCurrentLocation();
          });
        } else {
          Alert.alert('Permission Denied', 'Location permission is required to use this feature.');
        }
      });
    } else {
      Location.requestForegroundPermissionsAsync().then((status) => {
        console.log('status', status.status)
        if (status.status === 'granted') {
          getCurrentLocation();
        } else {
          Alert.alert('Permission Denied', 'Location permission is required to use this feature.');
        }
      });
    }
  }, []);

  const getCurrentLocation = () => {
    console.log('getting location');

    Location.getCurrentPositionAsync({ accuracy: Location.Accuracy.High })
      .then((location) => {
          setRegion({
            ...region,
            latitude: location.coords.latitude,
            longitude: location.coords.longitude,
          });
          setLocation(true)
        console.log('correct located ', location.coords);
        }
      ) .catch((err) => {
      Alert.alert('Error', err.message);
      console.log(err.message);
    });
  };


  const zoomIn = () => {
    setRegion((prevRegion) => ({
      ...prevRegion,
      latitudeDelta: prevRegion.latitudeDelta / 2,
      longitudeDelta: prevRegion.longitudeDelta / 2,
    }));
  };

  const zoomOut = () => {
    setRegion((prevRegion) => ({
      ...prevRegion,
      latitudeDelta: prevRegion.latitudeDelta * 2,
      longitudeDelta: prevRegion.longitudeDelta * 2,
    }));
  };

  const onCategoryChange = async (category: string) => {
    console.log('Category change', category, searchText);
    setSelectedCategory(category);
    try {
      const attractions = await fetchAttractions(searchText, category);
      setAttractions(attractions);
    } catch (error) {
      console.error(error);
    }
  };

  const setNewRegion = (location: { latitude: number; longitude: number; }) => {
    setRegion({...region, latitude: location.latitude, longitude: location.longitude });
    console.log(attractions);
  }

  return (
    <View style={styles.container}>
      <Search
        setLocation={setNewRegion}
        fetchAttractions={fetchAttractions}
        setSearchText={setSearchText}
        searchText={searchText}
      />
      {location && (
        <MapView
          style={styles.map}
          region={region}
          provider={PROVIDER_DEFAULT}
        >
          <UrlTile
            urlTemplate="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            maximumZ={25}
          />

          <Marker
            coordinate={{ latitude: region.latitude, longitude: region.longitude }}
            title="Your localization"
            pinColor="blue"
          />

          {attractions.map((attraction: Attraction) => (
            <Marker
              key={attraction.id}
              coordinate={{
                latitude: attraction.latitude,
                longitude: attraction.longitude,
              }}
              title={attraction.name}
              description={attraction.description}
              // image={(attraction.image_url as ImageURISource)
              //   || 'https://media.cntraveler.com/photos/58de89946c3567139f9b6cca/16:9/w_1920,c_limit/GettyImages-468366251.jpg'}
            />
          ))}
        </MapView>
      )}
      <View style={styles.zoomControls}>
        <Button title="+" onPress={zoomIn} />
        <View style={styles.spacer} />
        <Button title="-" onPress={zoomOut} />
      </View>
      <BottomPanel
        isVisible={panelVisible}
        searchText={searchText}
        selectedCategory={selectedCategory}
        onCategoryChange={onCategoryChange}
        attractions={attractions}
      />
    </View>
  );
};

export default OsmBoard;
