import React, { useState } from 'react';
import { Route } from "../types";
import { routesExample } from "../api/fake/apiMock";
import { RouteTileFull } from "./components/RouteTileFull";

type routesListType = {
  short: boolean;
}

const RoutesList: React.FC<{listType : routesListType}> = ({ listType }) => {
  const [userRoutes, setUserRoutes] = useState<Route[]>(routesExample);
  return (
    <>
      {!listType?.short &&
      <RouteTileFull routes={userRoutes}/>
      }
    </>
  )
};

export default RoutesList;