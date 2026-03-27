import mongoose, { Schema, Document } from "mongoose";

export interface IZone extends Document {
  zoneId: string;
  zoneName: string;
  description: string;
  climateCondition: string;
  minTemp: number;
  maxTemp: number;
  deviceId: string; 
}

const ZoneSchema: Schema = new Schema(
  {
    zoneId: { type: String, required: true, unique: true },
    zoneName: { type: String, required: true },
    description: { type: String },
    climateCondition: { type: String },
    minTemp: { type: Number, required: true },
    maxTemp: { type: Number, required: true },
    deviceId: { type: String },
  },
  { timestamps: true },
);

export default mongoose.model<IZone>("Zone", ZoneSchema);
