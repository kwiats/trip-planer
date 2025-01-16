import React, { useEffect, useState } from 'react';
import { ScrollView, Text, TouchableOpacity, View } from 'react-native';
import { attractionDetails, imagePlaceholder } from './styles';
import { Attraction, NavigationProps, Opinion } from '../Attraction/types';
import { fetchAttraction } from '../Attraction/api/attractionsApi';
import { attractionsExamples } from '../Attraction/api/fake/apiMock';
import EditSubMenuModal from './components/details/edit/EditSubMenu';
import ReviewsModal from './components/details/review/ReviewsModal';
import RoutesList from "../Route/RoutesList/RoutesList";

type AttractionDetailsPops = {
  route: { params: { id: number } };
  navigation: NavigationProps;
}

const AttractionDetailScreen: React.FC<AttractionDetailsPops> = ({ route, navigation }) => {
  const [attractionData, setAttractionData] = useState<Attraction>();
  const [attractionImages, setAttractionImages] = useState<any>();
  const [favorite, setFavorite] = useState<boolean>(false);
  const [editMenuVisible, setEditMenuVisible] = useState<boolean>(false);
  const [reviewsModalVisible, setReviewsModalVisible] = useState<boolean>(false);
  const [routesListVisible, setRoutesListVisible] = useState<boolean>(false);
  const userId = 1; //ToDo it's temporary

  useEffect(() => {
    const attractionId = route.params.id;
    fetchAttraction(attractionId)
      .then((attraction) => setAttractionData(attraction))
      .catch(() => {
        setAttractionData(attractionsExamples.find((attraction) => attraction.id === attractionId));
        console.error('Error', 'Failed getting attraction. Loading attraction demo data');
      });
    //Add another fetches
    setAttractionImages(
      Array.from({ length: 3 }, (_, index) => (
        <View key={index} style={imagePlaceholder.placeholder}/>
      ))
    );
  }, [route.params.id]);

  const editBox = (attractionAuthor: number | undefined) => {
    if (attractionAuthor && attractionAuthor === userId) {
      return (
        <TouchableOpacity onPress={() => setEditMenuVisible(true)}>
          <Text style={attractionDetails.name}>✎</Text>
        </TouchableOpacity>
      );
    }
  };

  const onGeneralRatingClick = () => {
    setReviewsModalVisible(true);
  };

  return attractionDetails ? (
    <>
      <ScrollView style={attractionDetails.container}>
        <View style={attractionDetails.header}>
          <Text style={attractionDetails.name}>
            {attractionData?.name} {editBox(attractionData?.user_id)}
          </Text>
          <EditSubMenuModal
            Id={attractionData?.id}
            visible={editMenuVisible}
            hideMenu={() => setEditMenuVisible(false)}
            edit={() => console.log('edit attraction')}
          />
          <TouchableOpacity
            style={attractionDetails.ratingContainer}
            onPress={onGeneralRatingClick}>
            <View style={attractionDetails.ratingBox}>
              <Text style={attractionDetails.ratingText}>{attractionData?.rating.toFixed(1)}</Text>
              <View style={attractionDetails.addOpinionIcon}>
                <Text style={attractionDetails.addOpinionText}>+</Text>
              </View>
            </View>
          </TouchableOpacity>
          <ReviewsModal
            attractionId={attractionData?.id as number}
            visible={reviewsModalVisible}
            hideMenu={() => setReviewsModalVisible(false)}
            onNewReview={() => navigation.navigate('NewReviewScreen')}
            onEditReview={(opinion: Opinion) =>
              navigation.navigate('EditReviewScreen', { review: opinion })
            }
          />
        </View>

        <View style={attractionDetails.categoryContainer}>
          <Text style={attractionDetails.category}>{attractionData?.category}</Text>
          <Text style={attractionDetails.views}>{attractionData?.visits} visits</Text>
        </View>

        <ScrollView horizontal style={attractionDetails.imageContainer}>
          <View style={imagePlaceholder.imageContainer}>{attractionImages}</View>
        </ScrollView>

        <View style={attractionDetails.openingHoursContainer}>
          <Text style={attractionDetails.openingHours}>
            ⌚ {attractionData?.open_hours?.open} - {attractionData?.open_hours?.close}
          </Text>
          <Text style={attractionDetails.price}>$$ {attractionData?.price}</Text>
        </View>

        <Text style={attractionDetails.description}>{attractionData?.description}</Text>
      </ScrollView>

      <View style={attractionDetails.buttonsContainer}>
        <TouchableOpacity
          style={attractionDetails.addToRouteButton}
          onPress={() => setRoutesListVisible(!routesListVisible)}>
          <Text style={attractionDetails.addToRouteText}>Add to route</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={attractionDetails.favoriteButton}
          onPress={() => setFavorite(!favorite)}>
          <Text style={attractionDetails.favoriteText}>{favorite ? '❤️' : '♡'}</Text>
        </TouchableOpacity>
      </View>
      {routesListVisible && <RoutesList short={true} isOpen={true}/>}
    </>
  ) : (
    <Text> Loading or something else</Text>
  );
};

export default AttractionDetailScreen;
