import React, { useContext } from 'react';
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer';
import AttractionSubMenu from '../../components/views/Attraction/Router';
import TestSubMenu from '../../components/views/test/Router';
import { AuthContext } from "../../contexts/AuthContext";
import RouteSubMenu from "../../components/views/Route/Router";

//Here, instead of any, you need to create an interface, but I don't know how yet
const SubMenuDrawerContent: React.FC<any> = (props) => {
  const { userToken } = useContext(AuthContext);
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      {userToken && <AttractionSubMenu {...props} /> }
      {userToken && <RouteSubMenu {...props} /> }
      <TestSubMenu {...props} />
    </DrawerContentScrollView>
  );
};

export default SubMenuDrawerContent;
