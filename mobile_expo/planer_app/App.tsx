import React from 'react';

import { View } from 'react-native';
import styles from './Styles';
import Router from './routers/Router';
import { AuthProvider } from './contexts/AuthContext';
import { GestureHandlerRootView } from "react-native-gesture-handler";

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
