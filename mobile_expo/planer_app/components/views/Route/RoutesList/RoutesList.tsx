import React, { useState } from 'react';
import { Route } from "../types";
import { routesExample } from "../api/fake/apiMock";
import { RouteTileFull } from "./components/RouteTileFull";
import { RouteTileShort } from "./components/RouteTileShort";

type routesListProps = {
  short: boolean;
  isOpen : boolean;
}

const RoutesList: React.FC<routesListProps> = ({ short, isOpen }) => {
  const [userRoutes, setUserRoutes] = useState<Route[]>(routesExample);

  const onClose = (id: number) => {
    console.log(id);
  };

  return (
    <>
      {!short &&
      <RouteTileFull routes={userRoutes}/>
      }
      {short &&
      <RouteTileShort routes={userRoutes} setRoutes={setUserRoutes} isOpen={isOpen} onClose={onClose} />
      }
    </>
  )
};

export default RoutesList;