import React, { useState } from 'react';
import { DrawerItem, DrawerNavigationProp } from '@react-navigation/drawer';
import { View } from 'react-native';

type DrawerParamList = {
  ShowRoutes: any;
  CreateRoute: any;
};

type RouteSubMenuProps = {
  navigation: DrawerNavigationProp<DrawerParamList>;
};

const RouteSubMenu: React.FC<RouteSubMenuProps> = (props) => {
  const [nestedMenuToggle, setNestedMenuToggle] = useState(false);
  const navigation = props.navigation;

  return (
    <>
      <DrawerItem
        label="My Routes"
        onPress={() => setNestedMenuToggle(!nestedMenuToggle)}
        focused={nestedMenuToggle}
      />
      <View style={{ marginLeft: 16, display: nestedMenuToggle ? 'flex' : 'none' }}>
        <DrawerItem
          label="Show my routes"
          onPress={() => {
            navigation.navigate('ShowRoutes');
            setNestedMenuToggle(false);
          }}
        />
        <DrawerItem
          label="Create new route"
          onPress={() => {
            navigation.navigate('CreateRoute');
            setNestedMenuToggle(false);
          }}
        />
      </View>
    </>
  );
};

export default RouteSubMenu;