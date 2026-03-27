import mongoose, { Schema, Document } from "mongoose";

export interface IZone extends Document {
  zoneId: string;
  zoneName: string;
  description: string;
  climateCondition: string;
}

const ZoneSchema: Schema = new Schema(
  {
    zoneId: { type: String, required: true, unique: true },
    zoneName: { type: String, required: true },
    description: { type: String },
    climateCondition: { type: String },
  },
  { timestamps: true },
);

export default mongoose.model<IZone>("Zone", ZoneSchema);
