import React, { useState } from 'react';
import { View } from 'react-native';
import { styles } from './styles';
import MapboxBoard from './components/MapBoard';
import RoutesList from "../Route/RoutesList/RoutesList";

const Dashboard = () => {
  const [routesListVisible, setRoutesListVisible] = useState<boolean>(false);
  return (
    <>
      <RoutesList short={true} isOpen={routesListVisible}/>
      <View style={styles.page}>
        <MapboxBoard
          onAddToRoadClick={() => setRoutesListVisible(true)}
        />
      </View>
    </>
  );
};

export default Dashboard;
