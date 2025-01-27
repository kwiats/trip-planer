import React, { useEffect, useState } from "react";
import { FlatList, Text, TextInput, TouchableOpacity, View } from "react-native";
import DraggableFlatList from "react-native-draggable-flatlist";
import { routesDetails as styles } from "../styles";
import { Attraction } from "../../Attraction/types";
import { Route } from "../types";
import { getStatusIcon } from "../../../utils/statusIcon";
import AttractionTile from "./components/AttractionTile";
import StatusDropdown from "./components/StatusDropdown";

interface routeDetailsProps {
  route: {
    params: {
      target: Route;
    }
  }
}

const RouteDetails: React.FC<routeDetailsProps> = ({ route }) => {

  const { target } = route.params;
  const [isEditing, setIsEditing] = useState<boolean>(false);
  const [targetRoute, setTargetRoute] = useState<Route>(target);

  useEffect(() => {
    setTargetRoute(target);
  }, [target]);

  const handleApplyChanges = () => {
    console.log('change route: ', targetRoute.id);
    setIsEditing(false);
  };

  const handleAbortChanges = () => {
    setTargetRoute(target);
    setIsEditing(false);
  };

  const onRemoveAttraction = (attraction: Attraction) => {
    console.log('remove attraction: ', attraction.id);
    setTargetRoute((prev) => ({
      ...prev,
      attractions: prev.attractions.filter((attr) => attr.id !== attraction.id),
    }))
  }

  const renderEditAttractionTile = ({ item, drag, isActive }: {
    item: Attraction;
    drag: () => void;
    isActive: boolean;
  }) => {
    return (
      <TouchableOpacity onLongPress={drag} disabled={isActive}>
        <AttractionTile
          attraction={item}
          editeMode={isEditing}
          onRemove={() => onRemoveAttraction(item)}
        />
      </TouchableOpacity>
    );
  };

  return (
    <View style={styles.container}>
      {isEditing ? (
        <View>
          <View style={styles.titleContainer}>
            <TextInput
              style={styles.titleInput}
              value={targetRoute.name}
              onChangeText={(text) =>
                setTargetRoute((prev) => ({ ...prev, name: text }))
              }
              placeholder="Route Name"
            />
            <StatusDropdown currentStatus={targetRoute.status} onStatusChange={(S) =>
              setTargetRoute((prev) => ({ ...prev, status: S }))
            }/>
            <TouchableOpacity
              style={styles.applyButton}
              onPress={() => {
                handleApplyChanges()
                setIsEditing(false);
              }}
            >
              <Text style={styles.applyButtonText}>✅</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.inputBorder}>
            <View style={styles.descriptionContainer}>
              <TextInput
                style={styles.descriptionInput}
                value={targetRoute.description != "null" ?
                  targetRoute.description :
                  "// not described //"}
                onChangeText={(text) =>
                  setTargetRoute((prev) => ({ ...prev, description: text }))
                }
                placeholder="Route Description"
                multiline
              />
            </View>
          </View>
          <DraggableFlatList
            data={targetRoute.attractions}
            keyExtractor={(item) => item.id.toString()}
            onDragEnd={({ data }) =>
              setTargetRoute((prev) => ({ ...prev, attractions: data }))
            }
            renderItem={renderEditAttractionTile}
          />
        </View>
      ) : (
        <View>
          <View style={styles.titleContainer}>
            <Text style={styles.title}>{targetRoute.name}</Text>
            <Text style={styles.statusIcon}>{getStatusIcon(targetRoute.status)}</Text>
            <TouchableOpacity
              style={styles.editButton}
              onPress={() => setIsEditing(true)}
            >
              <Text style={styles.editButtonText}>Edit</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.descriptionContainer}>
            <Text style={styles.description}>{targetRoute.description != "null" ?
              targetRoute.description :
              "// not described //"}
            </Text>
          </View>
          <FlatList
            data={targetRoute.attractions}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => (
              <AttractionTile attraction={item} editeMode={isEditing}/>
            )}
          />
        </View>
      )}
    </View>
  );
};

export default RouteDetails;