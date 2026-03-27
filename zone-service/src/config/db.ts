import mongoose from "mongoose";

export const connectDB = async () => {
  const MONGO_URL = process.env.MONGO_URI as string;
  try {
    const conn = await mongoose.connect(MONGO_URL);
    console.log(`✅ MongoDB Connected: ${conn.connection.host}`);
  } catch (error) {
    console.error(`❌ Error: ${error}`);
    process.exit(1);
  }
};
