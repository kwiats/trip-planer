import React, { useState } from 'react';
import { Route } from "../types";
import { routesExample } from "../api/fake/apiMock";
import { RouteTileFull } from "./components/RouteTileFull";
import { RouteTileShort } from "./components/RouteTileShort";

type routesListProps = {
  short: boolean;
  isOpen: boolean;
  onClose: () => void;
}

const RoutesList: React.FC<routesListProps> = ({ short, isOpen, onClose }) => {
  const [userRoutes, setUserRoutes] = useState<Route[]>(routesExample);

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
              onShowDetails={() => console.log('Route details')}
              onDeleteRoute={() => console.log('Delete route')}
          />
      }
      {short &&
          <RouteTileShort routes={userRoutes} setRoutes={setUserRoutes} isOpen={isOpen} onClose={onModalClose}/>
      }
    </>
  )
};

export default RoutesList;