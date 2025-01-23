import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  page: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  container: {
    height: '100%',
    width: '100%',
  },
  errorText: {
    fontSize: 24,
    color: 'red',
  },
  map: {
    flex: 1,
  },
  searchInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 10,
    margin: 10,
  },
  searchButton: {
    height: 40,
    backgroundColor: '#2196F3',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 5,
    margin: 10,
    paddingHorizontal: 20,
  },
  searchSection: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  searchBottomPanelInput: {
    flex: 1,
    marginRight: 10,
  },
  picker: {
    flex: 1,
  },
  attractionsGrid: {
    flexDirection: 'column',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  attractionTile: {
    width: '100%',
    padding: 10,
    marginVertical: 5,
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
  },
  zoomControls: {
    position: 'absolute',
    top: 130,
    left: 10,
    flexDirection: 'column',
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    borderRadius: 8,
    padding: 5,
  },
  spacer: {
    height: 10,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
    marginBottom: 20,
  },
  button: {
    marginLeft: 8,
    paddingVertical: 10,
    paddingHorizontal: 16,
    borderRadius: 8,
    borderColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 13
  },
  buttonText: {
    color: '000',
    fontSize: 16,
    fontWeight: 'bold',
  },
  calloutContainer: {
    padding: 10,
    backgroundColor: '#FFF',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    elevation: 5,
    minWidth: 150,
    minHeight: 50
  },
  calloutView: {
    width: 160,
    height: 40,
  },
  calloutImage: {
    width: '100%',
    height: 100,
    borderRadius: 5,
    marginBottom: 10,
  },
  calloutTextContainer: {
    flex: 1,
  },
  calloutText: {
    color: '#085760',
    fontSize: 16,
  },
  calloutTitle: {
    fontWeight: 'bold',
    fontSize: 16,
    marginBottom: 5,
  },
  calloutDescription: {
    fontSize: 14,
    color: 'gray',
    marginBottom: 10,
  },
  calloutButtonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  calloutButton: {
    backgroundColor: '#007bff',
    paddingVertical: 5,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  calloutButtonText: {
    color: 'white',
    fontSize: 12,
  },
});
