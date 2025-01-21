import React, { useState } from 'react';
import { View } from 'react-native';
import { styles } from './styles';
import MapboxBoard from './components/MapBoard';
import RoutesList from "../Route/RoutesList/RoutesList";

const Dashboard = () => {
  // const [routesListVisible, setRoutesListVisible] = useState<boolean>(true);
  return (
    <>
    {/*{routesListVisible && <RoutesList short={true} isOpen={true}/>}*/}
      <View style={styles.page}>
        <MapboxBoard
          onAddToRoadClick={() => null } //setRoutesListVisible(true)}
        />
      </View>
    </>
  );
};

export default Dashboard;
