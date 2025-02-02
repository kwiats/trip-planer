import React, { useState } from 'react';
import { Route } from "../types";
import { routesExample } from "../api/fake/apiMock";
import { RouteTileFull } from "./components/RouteTileFull";
import { RouteTileShort } from "./components/RouteTileShort";
import { useNavigation } from "@react-navigation/native";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";
import { DrawerParamList } from "../../../../routers/DrawerParamList";

type RoutesListProps = {
  short: boolean;
  isOpen: boolean;
  onClose: () => void;
}

const RoutesList: React.FC<RoutesListProps> = ({ short, isOpen, onClose }) => {
  const [userRoutes, setUserRoutes] = useState<Route[]>(routesExample);
  const navigation = useNavigation<NativeStackNavigationProp<DrawerParamList>>();

  const onModalClose = (id: number) => {
    console.log(id);
    onClose();
  };

  return (
    <>
      {!short &&
          <RouteTileFull
              routes={userRoutes}
              setRoutes={setUserRoutes}
              onShowOnMap={() => console.log('Show on map')}
              onShowDetails={(target) => {
                navigation.navigate('Route Details', { target });
              }}
              onDeleteRoute={(target) => setUserRoutes(userRoutes.filter(route => route.id !== target.id))}
          />
      }
      {short &&
          <RouteTileShort routes={userRoutes} setRoutes={setUserRoutes} isOpen={isOpen} onClose={onModalClose}/>
      }
    </>
  )
};

export default RoutesList;