import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  footer: {
    height: 50,
    backgroundColor: 'gray',
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
  },
});
export const attractionTileStyles = StyleSheet.create({
  attractionTile: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 20,
    marginVertical: 10,
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
    width: 70,
    height: 70,
    borderRadius: 15,
  },
  emptyImage: {
    width: 70,
    height: 70,
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
  category: {
    fontSize: 14,
    color: 'grey',
    marginBottom: 10,
  },
  description: {
    fontSize: 12,
    color: 'grey',
  },
  rate: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFD700',
  },
});
export const imagePlaceholder = StyleSheet.create({
  imageContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 20,
  },
  placeholder: {
    width: 450,
    height: 300,
    backgroundColor: '#abc',
    marginRight: 10,
  },
});
export const attractionDetails = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    marginBottom: 110,
  },
  header: {
    padding: 5,
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 0,
    marginLeft: 7,
    marginRight: -10,
  },
  name: {
    flex: 3,
    fontFamily: 'Inter',
    fontSize: 32,
    color: '#000',
    fontWeight: 'bold',
  },
  ratingContainer: {
    flex: 1,
    alignItems: 'flex-end',
    flexDirection: 'row',
    justifyContent: 'flex-end',
  },
  ratingBox: {
    width: 65,
    height: 65,
    backgroundColor: '#D9D9D9',
    borderRadius: 33,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 2,
    marginRight: 13
  },
  ratingText: {
    color: '#131111',
    fontSize: 20,
    fontFamily: 'Inter',
    fontWeight: 'bold',
  },
  addOpinionIcon: {
    width: 21,
    height: 21,
    borderRadius: 11,
    backgroundColor: 'black',
    alignItems: 'center',
    marginLeft: -10,
    marginRight: -50,
    marginTop: 2,
    marginBottom: -18
  },
  categoryContainer: {
    padding: 5,
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 0,
    marginLeft: 12,
    marginRight: -89,
  },
  category: {
    flex: 3,
    fontFamily: 'Inter',
    fontSize: 20,
    color: '#6D6666',
  },
  views: {
    flex: 2,
    fontFamily: 'Inter',
    fontSize: 20,
    color: '#6D6666',
  },
  imageContainer: {
    height: 305,
    marginLeft: -69,
  },
  openingHoursContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 5,
    marginTop: 10,
  },
  openingHours: {
    marginLeft: 18,
    fontFamily: 'Inter',
    fontSize: 20,
    color: '#6D6666',
  },
  price: {
    marginRight: 5,
    fontFamily: 'Inter',
    fontSize: 20,
    color: '#6D6666',
  },
  description: {
    padding: 5,
    marginTop: 8,
    marginLeft: 13,
    fontFamily: 'Inter',
    fontSize: 20,
    color: '#909090',
    fontWeight: '800',
  },
  buttonsContainer: {
    position: 'absolute',
    bottom: 10,
    left: 0,
    right: 0,
    flexDirection: 'row',
    justifyContent: 'space-between',
    padding: 5,
    backgroundColor: '#fff',
  },
  addToRouteButton: {
    width: 268,
    height: 69,
    backgroundColor: '#D5D2D2',
    borderRadius: 35,
    marginBottom: 20,
    marginLeft: 10,
    shadowColor: '#000',
    shadowOffset: { width: 4, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 5,
    justifyContent: 'center',
    alignItems: 'center',
  },
  addToRouteText: {
    fontFamily: 'Inter',
    fontSize: 22,
    color: '#0C0C0C',
    fontWeight: 'bold',
  },
  favoriteButton: {
    width: 65,
    height: 65,
    marginTop: 2,
    marginRight: 10,
    backgroundColor: '#D5D2D2',
    borderRadius: 33,
    justifyContent: 'center',
    alignItems: 'center',
  },
  favoriteText: {
    color: 'red',
    fontSize: 24,
  },
  addOpinionText: {
    fontSize: 15,
    color: '#fff',
    fontWeight: 'bold' 
  }
});
