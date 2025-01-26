import React from 'react';

import { View } from 'react-native';
import styles from './Styles';
import Router from './routers/Router';
import { AuthProvider } from './contexts/AuthContext';
import { GestureHandlerRootView } from "react-native-gesture-handler";
import { DrawerParamList } from "./routers/DrawerParamList";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Stack = createNativeStackNavigator<DrawerParamList>();

function App(): React.JSX.Element {
  return (
    <AuthProvider>
      <GestureHandlerRootView>
        <View style={styles.container}>
          <Router/>
        </View>
      </GestureHandlerRootView>
    </AuthProvider>
  );
}

export default App;
