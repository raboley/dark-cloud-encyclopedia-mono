// export interface IWeapon {
//   weaponId: number;
//   weaponName: string;
//   weaponCode: string;
//   releaseDate: string;
//   price: number;
//   description: string;
//   starRating: number;
//   imageUrl: string;
// }

export interface IWeapon {
  weaponId: number
  characterName: string;
  weaponName: string;
  tier: number;
  obtainedFrom: IObtainedFrom;
  weaponThumbnail: string;
  weaponImageUrls: any[];
}
export interface IObtainedFrom {
  DivineBeastCave: string;
  WiseOwlForest: string;
  Shipwreck: string;
  SunandMoonTemple: string;
  MoonSea: string;
  GallertyofTime: string;
  DemonShaft: string;
  Gift: string;
  Buy: string;
  Evolution: string;
}