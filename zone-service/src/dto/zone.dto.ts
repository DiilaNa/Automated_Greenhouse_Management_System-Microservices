export interface CreateZoneDTO {
  zoneId: string;
  zoneName: string;
  description?: string;
  climateCondition?: string;
  minTemp: number; 
  maxTemp: number;
}

export interface UpdateZoneDTO {
  zoneName?: string;
  description?: string;
  climateCondition?: string;
  minTemp?: number;
  maxTemp?: number;
}
