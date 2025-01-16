import React, { useEffect, useState } from "react";
import { Route } from "../../types";
import {
  FlatList,
  Keyboard,
  Modal,
  Text,
  TextInput,
  TouchableOpacity,
  TouchableWithoutFeedback,
  View
} from "react-native";
import { routesListShort as styles } from "../../styles";

interface RouteListProps {
  routes: Route[];
  setRoutes: React.Dispatch<React.SetStateAction<Route[]>>;
  isOpen: boolean;
  onClose: (id: number) => void;
}

export const RouteTileShort: React.FC<RouteListProps> = ({ routes, setRoutes, isOpen, onClose }) => {

  const [newRouteName, setNewRouteName] = useState('');
  const [isModalVisible, setModalVisible] = useState<boolean>(isOpen);

  useEffect(() => {
    setModalVisible(isOpen);
  }, [isOpen]);

  const addRoute = () => {
    if (newRouteName.trim()) {
      const id = routes.length + 1;
      setRoutes((prevRoutes) => [
        ...prevRoutes,
        {
          id: id,
          name: newRouteName,
          description: '',
          attractions: [],
        },
      ]);
      setNewRouteName('');
      setModalVisible(false);
      onClose(id);
    }
  };

  return (
    <Modal
      animationType="slide"
      transparent
      visible={isModalVisible}
      onRequestClose={() => setModalVisible(false)}
    >
      <TouchableWithoutFeedback
        onPress={() => {
          setModalVisible(false);
          Keyboard.dismiss();
        }}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            <Text style={styles.modalTitle}>Routes</Text>
            <FlatList
              data={routes}
              renderItem={({ item }) => (
                <View style={styles.listItem}>
                  <TouchableOpacity onPress={() => {
                    setModalVisible(false);
                    onClose(item.id);
                  }}>
                    <Text style={styles.listItemText}>{item.name}</Text>
                  </TouchableOpacity>
                </View>
              )}
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
                <Text style={styles.addButtonText}>Add New</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </TouchableWithoutFeedback>
    </Modal>

  );
};