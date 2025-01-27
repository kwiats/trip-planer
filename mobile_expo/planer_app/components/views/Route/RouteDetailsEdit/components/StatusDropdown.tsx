import React, { useState } from "react";
import { View, Text, TouchableOpacity, FlatList, StyleSheet } from "react-native";
import { getStatusIcon } from "../../../../utils/statusIcon";
import {dropdown as styles} from "../../styles";

interface StatusDropdownProps {
  currentStatus: string;
  onStatusChange: (newStatus: string) => void;
}

const statusOptions = [
  { label: "New", value: "new" },
  { label: "Active", value: "active" },
  { label: "Completed", value: "completed" },
];

const StatusDropdown: React.FC<StatusDropdownProps> = ({
                                                         currentStatus,
                                                         onStatusChange,
                                                       }) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const handleStatusSelect = (status: string) => {
    onStatusChange(status);
    setIsDropdownOpen(false);
  };

  return (
    <View style={styles.container}>
      <TouchableOpacity
        style={styles.selectedStatus}
        onPress={() => setIsDropdownOpen(!isDropdownOpen)}
      >
        <Text style={styles.statusIcon}>{getStatusIcon(currentStatus)}</Text>
      </TouchableOpacity>

      {isDropdownOpen && (
        <View style={styles.dropdown}>
          <FlatList
            data={statusOptions}
            keyExtractor={(item) => item.value}
            renderItem={({ item }) => (
              <TouchableOpacity
                style={styles.dropdownItem}
                onPress={() => handleStatusSelect(item.value)}
              >
                <Text style={styles.dropdownText}>
                  {getStatusIcon(item.value)}
                </Text>
              </TouchableOpacity>
            )}
          />
        </View>
      )}
    </View>
  );
};

export default StatusDropdown;
