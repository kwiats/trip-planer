import { Route } from "../../types";

export const routesExample: Route[] = [
  {
    id: 1,
    name: 'exampleRoute1',
    description: 'null',
    attractions: [
      {
        id: 1,
        name: 'Royal Castle',
        user_id: 1,
        country: 'Poland',
        city: 'Warsaw',
        region: 'Masovian',
        category: 'Culture',
        description: 'Beautiful castle in the heart of Warsaw.',
        rating: 4,
        latitude: 52.2474,
        longitude: 21.0147,
        open_hours: { open: 9, close: 18 },
        address: 'Castle Square',
        time_spent: 2,
        price: 20,
        visits: 500,
      },
      {
        id: 2,
        name: 'Wawel Castle',
        user_id: 2,
        country: 'Poland',
        city: 'Krakow',
        region: 'Lesser Poland',
        category: 'Culture',
        description: 'Historic castle in Krakow.',
        rating: 4,
        latitude: 50.0547,
        longitude: 19.9354,
        open_hours: { open: 10, close: 17 },
        address: 'Wawel 5',
        time_spent: 3,
        price: 25,
        visits: 700,
      },
    ],
    status: 'active'
  },
  {
    id: 2,
    name: 'exampleRoute2',
    description: 'null',
    attractions: [],
    status: 'completed'
  },
  {
    id: 3,
    name: 'exampleRoute3',
    description: 'null',
    attractions: [
      {
        id: 3,
        name: 'Malbork Castle',
        user_id: 3,
        country: 'Poland',
        city: 'Malbork',
        region: 'Pomeranian',
        category: 'Culture',
        description: 'World\'s largest brick castle.',
        rating: 5,
        latitude: 54.0389,
        longitude: 19.0284,
        open_hours: { open: 10, close: 16 },
        address: 'Stare Miasto 1',
        time_spent: 4,
        price: 30,
        visits: 1000,
      },
      {
        id: 4,
        name: 'Berlin Wall',
        user_id: 1,
        country: 'Germany',
        city: 'Berlin',
        region: 'Brandenburg',
        category: 'Culture',
        description: 'Remnant of the Cold War.',
        rating: 3,
        latitude: 52.5074,
        longitude: 13.4395,
        open_hours: { open: 8, close: 20 },
        address: 'Bernauer Strasse 111',
        time_spent: 2,
        price: 15,
        visits: 400,
      },
      {
        id: 5,
        name: 'Neuschwanstein Castle',
        user_id: 2,
        country: 'Germany',
        city: 'Füssen',
        region: 'Bavaria',
        category: 'Culture',
        description: 'Fairytale castle in the Bavarian Alps.',
        rating: 5,
        latitude: 47.5576,
        longitude: 10.7498,
        open_hours: { open: 9, close: 18 },
        address: 'Neuschwansteinstrasse 20',
        time_spent: 5,
        price: 35,
        visits: 1200,
      },
    ],
    status: 'completed'
  },
  {
    id: 4,
    name: 'exampleRoute4',
    description: 'null',
    attractions: [],
    status: 'active'
  }
]