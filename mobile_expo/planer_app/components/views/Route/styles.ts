import { StyleSheet } from "react-native";

export const routesList = StyleSheet.create({
  contentContainer: {
    flex: 1,
    width: '100%',
    justifyContent: "center",
    alignItems: "center",
    position: 'absolute',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: "rgba(0, 0, 0, 0.5)",
    justifyContent: "center",
    alignItems: "center",
  },
  container: {
    width: "90%",
    backgroundColor: "#fff",
    borderRadius: 16,
    padding: 20,
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 6,
    elevation: 10,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#333",
    marginBottom: 16,
  },
  listItem: {
    paddingVertical: 12,
    paddingHorizontal: 16,
    marginVertical: 8,
    backgroundColor: "#f9f9f9",
    borderRadius: 12,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  listItemText: {
    fontSize: 18,
    fontWeight: "600",
    color: "#333",
  },
  listItemSubText: {
    fontSize: 14,
    color: "#666",
    marginTop: 4,
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginTop: 16,
    width: "100%",
  },
  input: {
    flex: 1,
    height: 48,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 12,
    paddingHorizontal: 16,
    fontSize: 16,
    color: "#333",
    backgroundColor: "#fefefe",
  },
  addButton: {
    marginLeft: 12,
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 12,
    backgroundColor: "#4CAF50",
    justifyContent: "center",
    alignItems: "center",
  },
  addButtonText: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  buttonGroup: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 12,
  },
  actionButton: {
    flex: 1,
    marginHorizontal: 4,
    paddingVertical: 10,
    borderRadius: 8,
    backgroundColor: "#2196F3",
    justifyContent: "center",
    alignItems: "center",
  },
  actionButtonText: {
    color: "#fff",
    fontSize: 14,
    fontWeight: "600",
  },
});

export const routesDetails = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
  },
  inputBorder: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
  },
  titleContainer: {
    flexDirection: "row",
    alignItems: 'baseline',
    justifyContent: "space-between",
    padding: 10
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 8,
    width: '50%'
  },
  titleInput: {
    fontSize: 24,
    fontWeight: 'bold',
    fontStyle: 'italic',
    width: '50%',
    marginBottom: 8,
  },
  statusIcon: {
    fontSize: 30,
    fontWeight: 'bold'
  },
  descriptionContainer: {
    width: '100%',
    height: 40,
    marginBottom: 16,
  },
  description: {
    fontSize: 16,
    color: '#666',
  },
  descriptionInput: {
    fontSize: 16,
    color: '#666',
    fontStyle: 'italic',
  },
  attractionItem: {
    padding: 12,
    marginBottom: 8,
    backgroundColor: '#f9f9f9',
    borderRadius: 8,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  attractionName: {
    fontSize: 16,
  },
  removeButton: {
    backgroundColor: '#ff4d4d',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
  },
  removeButtonText: {
    color: '#fff',
    fontSize: 14,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 8,
    borderRadius: 8,
    marginBottom: 12,
  },
  textArea: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 8,
    borderRadius: 8,
    height: 100,
    textAlignVertical: 'top',
    marginBottom: 12,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 16,
  },
  editButton: {
    alignSelf: 'flex-end',
    backgroundColor: '#007bff',
    padding: 12,
    borderRadius: 8,
  },
  editButtonText: {
    color: '#fff',
    fontSize: 16,
  },
  applyButton: {
    alignSelf: 'flex-end',
    justifyContent: 'center',
    paddingBottom: 18,
  },
  applyButtonText: {
    fontSize: 36,
  },
  abortButton: {
    backgroundColor: '#dc3545',
    padding: 12,
    borderRadius: 8,
    flex: 1,
  },
  abortButtonText: {
    color: '#fff',
    textAlign: 'center',
    fontSize: 16,
  },
});

export const attractionTileStyles = StyleSheet.create(
  {
    attractionTile: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
      backgroundColor: '#fff',
      padding: 10,
      marginVertical: 5,
      borderRadius: 10,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.1,
      shadowRadius: 3,
      elevation: 2,
      width: '100%',
    },
    leftContainer: {
      flexDirection: 'row',
      flex: 1,
      alignItems: 'center',
    },
    imageContainer: {
      marginRight: 15,
    },
    image: {
      width: 50,
      height: 50,
      borderRadius: 15,
    },
    emptyImage: {
      width: 50,
      height: 50,
      borderRadius: 15,
      borderWidth: 1,
      borderColor: '#000',
      backgroundColor: 'transparent',
    },
    textContainer: {
      flexShrink: 1,
    },
    title: {
      fontWeight: 'bold',
      fontSize: 18,
      color: '#000',
    },
    subInfoContainer: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      marginBottom: 10,
    },
    subInfo: {
      fontSize: 14,
      color: 'gray',
    },
    rate: {
      fontSize: 21,
      fontWeight: 'bold',
      color: '#FFD700',
      marginRight: 10,
    },
    handle: {
      marginRight: 10,
      marginLeft: -5,
      fontSize: 18,
      fontWeight: 'bold',
      color: 'gray'
    },
    remove: {
      marginRight: -5,
      marginLeft: 5,
      fontSize: 21,
      fontWeight: 'bold',
      color: 'red',
    }
  });

export const dropdown = StyleSheet.create({
  container: {
    position: "relative",
    zIndex: 1,
  },
  selectedStatus: {
    flexDirection: "row",
    alignItems: "center",
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
  },
  statusIcon: {
    fontSize: 30,
  },
  dropdown: {
    position: "absolute",
    top: 50,
    left: 0,
    right: 0,
    backgroundColor: "white",
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
    padding: 5,
  },
  dropdownItem: {
    padding: 10,
    flexDirection: "row",
    alignItems: "center",
  },
  dropdownText: {
    fontSize: 18,
  },
});