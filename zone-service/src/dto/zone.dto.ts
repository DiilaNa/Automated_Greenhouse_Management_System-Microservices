export interface CreateZoneDTO {
  zoneId: string;
  zoneName: string;
  description?: string;
  climateCondition?: string;
}

export interface UpdateZoneDTO {
  zoneName?: string;
  description?: string;
  climateCondition?: string;
}
