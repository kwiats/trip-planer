import React, { useEffect, useState } from 'react';
import { Alert, PermissionsAndroid, Platform, View } from 'react-native';
import MapView, { Marker, UrlTile } from 'react-native-maps';
import Geolocation from 'react-native-geolocation-service';
import * as Location from 'expo-location';
import { styles } from '../styles';
import Search from './Search';
import BottomPanel from './BottomPanel';
import { fetchAttractions } from '../api/attractionsApi';

const OsmBoard = () => {
  const [location, setLocation] = useState<any>(null); // Bieżąca lokalizacja użytkownika
  const [attractions, setAttractions] = useState<any>([]);
  const [panelVisible, setPanelVisible] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');

  useEffect(() => {
    console.log('efect');
    if (Platform.OS === 'android') {
      PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION, {
        title: 'Permission to access location',
        message: 'We need your permission to access your location',
        buttonNeutral: 'Ask Me Later',
        buttonNegative: 'Cancel',
        buttonPositive: 'OK',
      }).then((granted) => {
        if (granted === PermissionsAndroid.RESULTS.GRANTED) {
          console.log('granted')
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
          setLocation({
            latitude: location.coords.latitude,
            longitude: location.coords.longitude,
          });
        console.log('localization success');
          console.log(location.coords);
        }
      ) .catch((err) => {
      Alert.alert('Error', err.message);
      console.log(err.message);
    });

    // Geolocation.getCurrentPosition(
    //   (position) => {
    //     const { latitude, longitude } = position.coords;
    //     console.log({ latitude, longitude });
    //     setLocation({ latitude, longitude });
    //   },
    //   (error) => Alert.alert('Error', error.message),
    //   { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
    // );
  };

  const onCategoryChange = async (category: string) => {
    console.log('Zmiana kategorii', category, searchText);
    setSelectedCategory(category);
    try {
      const attractions = await fetchAttractions(searchText, category);
      setAttractions(attractions);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Search
        setLocation={setLocation}
        fetchAttractions={fetchAttractions}
        setSearchText={setSearchText}
        searchText={searchText}
      />
      {location && (
        <MapView
          style={styles.map}
          region={{
            latitude: location.latitude,
            longitude: location.longitude,
            latitudeDelta: 0.05,
            longitudeDelta: 0.05,
          }}
          // provider={null} // OSM używa domyślnego dostawcy
        >
          {/* Kafelki OpenStreetMap */}
          <UrlTile
            urlTemplate="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            maximumZ={19} // Maksymalne powiększenie mapy
          />

          {/* Marker bieżącej lokalizacji */}
          <Marker
            coordinate={{ latitude: location.latitude, longitude: location.longitude }}
            title="Twoja lokalizacja"
            pinColor="blue"
          />

          {/* Markery atrakcji */}
          {attractions.map((attraction: any) => (
            <Marker
              key={attraction.id}
              coordinate={{
                latitude: attraction.latitude,
                longitude: attraction.longitude,
              }}
              title={attraction.name}
            />
          ))}
        </MapView>
      )}
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
