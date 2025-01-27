import React, { useState } from "react";
import { Route } from "../../types";
import {
  FlatList,
  Keyboard,
  KeyboardAvoidingView,
  Platform,
  Text,
  TextInput,
  TouchableOpacity,
  View
} from "react-native";
import { routesList as styles } from "../../styles";
import { getStatusIcon } from "../../../../utils/statusIcon";

interface RouteListProps {
  routes: Route[];
  setRoutes: React.Dispatch<React.SetStateAction<Route[]>>;
  onShowOnMap: () => void;
  onShowDetails: (route: Route) => void;
  onDeleteRoute: (route: Route) => void;
}

export const RouteTileFull: React.FC<(RouteListProps)> = ({
                                                            routes,
                                                            setRoutes,
                                                            onShowOnMap,
                                                            onShowDetails,
                                                            onDeleteRoute,
                                                          }) => {
  const [selectedRouteId, setSelectedRouteId] = useState<number | null>(null);
  const [newRouteName, setNewRouteName] = useState<string>("");

  const countCitiesAndCountries = (attractions: any[]) => {
    const cities = new Set();
    const countries = new Set();

    attractions.forEach((attraction) => {
      if (attraction.city) cities.add(attraction.city);
      if (attraction.country) countries.add(attraction.country);
    });

    return { cityCount: cities.size, countryCount: countries.size };
  };

  const addRoute = () => {
    if (newRouteName.trim()) {
      const id = routes.length + 1;
      setRoutes((prevRoutes) => [
        ...prevRoutes,
        {
          id,
          name: newRouteName,
          description: "",
          attractions: [],
          status: "new",
        },
      ]);
      Keyboard.dismiss();
      setNewRouteName("");
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.contentContainer}
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      keyboardVerticalOffset={Platform.OS === "ios" ? 80 : 140}
    >
      <FlatList
        data={routes}
        style={{ width: "100%" }}
        renderItem={({ item: route }) => {
          const { cityCount, countryCount } = countCitiesAndCountries(route.attractions || []);
          const isSelected = selectedRouteId === route.id;

          return (
            <View style={styles.listItem}>
              <TouchableOpacity
                onPress={() => setSelectedRouteId(isSelected ? null : route.id)}
              >
                <Text style={styles.listItemText}>
                  {`${getStatusIcon(route.status)} ${route.name}`}
                </Text>
                <Text style={styles.listItemSubText}>
                  {`${route.attractions.length} attractions, ${cityCount} cities, ${countryCount} countries`}
                </Text>
              </TouchableOpacity>

              {isSelected && (
                <View style={styles.buttonGroup}>
                  {route.status != 'new' && <TouchableOpacity
                    style={styles.actionButton}
                    onPress={() => onShowOnMap()}
                  >
                    <Text style={styles.actionButtonText}>Show on Map</Text>
                  </TouchableOpacity>}
                  <TouchableOpacity
                    style={styles.actionButton}
                    onPress={() => {
                      setSelectedRouteId(null);
                      onShowDetails(route);
                    }}
                  >
                    <Text style={styles.actionButtonText}>{route.status ==='new' ? 'Create' : 'Details'}</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.actionButton}
                    onPress={() => onDeleteRoute(route)}
                  >
                    <Text style={styles.actionButtonText}>Delete</Text>
                  </TouchableOpacity>
                </View>
              )}
            </View>
          );
        }}
        keyExtractor={(item) => item.id.toString()}
      />
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="New route"
          value={newRouteName}
          onChangeText={setNewRouteName}
        />
        <TouchableOpacity style={styles.addButton} onPress={addRoute}>
          <Text style={styles.addButtonText}>Add</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
};
