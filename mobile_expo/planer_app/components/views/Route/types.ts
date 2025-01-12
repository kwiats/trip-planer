import { Attraction } from "../Attraction/types";

export type Route = {
  id: number;
  name: string;
  description: string;
  attractions: Attraction[];
}