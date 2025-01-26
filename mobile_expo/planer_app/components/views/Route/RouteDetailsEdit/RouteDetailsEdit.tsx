import React, { useState } from "react";
import { FlatList, Text, TextInput, TouchableOpacity, View } from "react-native";
import DraggableFlatList from "react-native-draggable-flatlist";
import { routesDetails as styles } from "../styles";
import {Attraction} from "../../Attraction/types";
import { Route } from "../types";

interface routeDetailsProps {
  route: {
    params: {
      target: Route;
      onUpdateRoute: (updatedRoute: Route) => void;
    }
  }
}

const RouteDetails: React.FC<routeDetailsProps> = ({ route }) => {

  const { target } = route.params;
  const [isEditing, setIsEditing] = useState<boolean>(false);
  const [editedRoute, setEditedRoute] = useState<Route>(target);

  const handleApplyChanges = () => {
    // onUpdateRoute(editedRoute);
    setIsEditing(false);
  };

  const handleAbortChanges = () => {
    setEditedRoute(target);
    setIsEditing(false);
  };

  const renderAttractionItem = ({ item, drag }: { item: Attraction; drag: () => void }) => (
    <TouchableOpacity
      style={styles.attractionItem}
      onLongPress={isEditing ? drag : undefined}
    >
      <Text style={styles.attractionName}>{item.name}</Text>
      {isEditing && (
        <TouchableOpacity
          style={styles.removeButton}
          onPress={() =>
            setEditedRoute((prev) => ({
              ...prev,
              attractions: prev.attractions.filter((attr) => attr.id !== item.id),
            }))
          }
        >
          <Text style={styles.removeButtonText}>Remove</Text>
        </TouchableOpacity>
      )}
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      {isEditing ? (
        <View>
          <TextInput
            style={styles.input}
            value={editedRoute.name}
            onChangeText={(text) =>
              setEditedRoute((prev) => ({ ...prev, name: text }))
            }
            placeholder="Route Name"
          />
          <TextInput
            style={styles.textArea}
            value={editedRoute.description}
            onChangeText={(text) =>
              setEditedRoute((prev) => ({ ...prev, description: text }))
            }
            placeholder="Route Description"
            multiline
          />
          <DraggableFlatList
            data={editedRoute.attractions}
            keyExtractor={(item) => item.id.toString()}
            onDragEnd={({ data }) =>
              setEditedRoute((prev) => ({ ...prev, attractions: data }))
            }
            renderItem={renderAttractionItem}
          />
          <View style={styles.buttonContainer}>
            <TouchableOpacity style={styles.applyButton} onPress={handleApplyChanges}>
              <Text style={styles.applyButtonText}>Apply</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.abortButton} onPress={handleAbortChanges}>
              <Text style={styles.abortButtonText}>Abort</Text>
            </TouchableOpacity>
          </View>
        </View>
      ) : (
        <View>
          <Text style={styles.title}>{target.name}</Text>
          <Text style={styles.description}>{target.description}</Text>
          <FlatList
            data={target.attractions}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => (
              <View style={styles.attractionItem}>
                <Text style={styles.attractionName}>{item.name}</Text>
              </View>
            )}
          />
          <TouchableOpacity
            style={styles.editButton}
            onPress={() => setIsEditing(true)}
          >
            <Text style={styles.editButtonText}>Edit</Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
};

export default RouteDetails;