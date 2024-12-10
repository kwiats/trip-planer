interface Coordinates {
    latitude: number;
    longitude: number;
  }

export const fetchLocationFromNominatim = (searchText: string): Promise<Coordinates> => {
  const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(
    searchText
  )}&format=json`;

  return fetch(url, {
    headers: {
      'User-Agent': 'YourAppName/1.0',
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data && data.length > 0) {
        const { lat, lon } = data[0];
        return { latitude: parseFloat(lat), longitude: parseFloat(lon) } as Coordinates;
      }
      throw new Error('No location found for the given search text');
    })
    .catch((error) => {
      console.error('Error during Nominatim geocoding:', error);
      throw error;
    });
};