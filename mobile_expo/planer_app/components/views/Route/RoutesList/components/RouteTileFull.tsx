import React, { Component } from "react";
import { Route } from "../../types";
import { FlatList, Text, View } from "react-native";

export const RouteTileFull: React.FC<{routes : Route[]}> = ({routes}) => {

  return (
    <FlatList data={routes} renderItem={({ item: route }) => (
      <View>
        <Text>
          {route.id + " - " + route.name + " - " + route.attractions}
        </Text>
      </View>
    )
    }/>
  )
}