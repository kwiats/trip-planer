import React, { useState } from 'react';
import { DrawerItem, DrawerNavigationProp } from '@react-navigation/drawer';
import { View } from 'react-native';

type DrawerSubList = {
  SearchAttraction: any;
  AddNewAttraction: any;
};

type AttractionSubMenuProps = {
  navigation: DrawerNavigationProp<DrawerSubList>;
};

const AttractionSubMenu: React.FC<AttractionSubMenuProps> = (props) => {
  const [nestedMenuToggle, setNestedMenuToggle] = useState(false);
  const navigation = props.navigation;

  return (
    <>
      <DrawerItem
        label="My Attractions"
        onPress={() => setNestedMenuToggle(!nestedMenuToggle)}
        focused={nestedMenuToggle}
      />
      <View style={{ marginLeft: 16, display: nestedMenuToggle ? 'flex' : 'none' }}>
        <DrawerItem
          label="Search"
          onPress={() => {
            navigation.navigate('SearchAttraction');
            setNestedMenuToggle(false);
          }}
        />
        <DrawerItem
          label="Add new"
          onPress={() => {
            navigation.navigate('AddNewAttraction');
            setNestedMenuToggle(false);
          }}
        />
      </View>
    </>
  );
};

export default AttractionSubMenu;
