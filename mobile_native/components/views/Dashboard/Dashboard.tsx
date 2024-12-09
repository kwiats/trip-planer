import React from 'react';
import { View } from 'react-native';
import { styles } from './styles';
import MapboxBoard from './components/MapboxBoard.tsx';

const Dashboard = () => {
  return (
    <View style={styles.page}>
      <MapboxBoard />
    </View>
  );
};

export default Dashboard;
