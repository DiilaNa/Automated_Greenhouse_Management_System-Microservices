import dotenv from "dotenv";
import express from "express";
import mongoose from "mongoose";

dotenv.config();

const SERVER_PORT = process.env.PORT || 8081;
const MONGO_URL = process.env.MONGO_URI as string;

const app = express();
app.use(express.json());


mongoose
  .connect(MONGO_URL)
  .then(() => console.log("✅ Zone Service connected to MongoDB"))
  .catch((err) => console.error("❌ MongoDB connection error:", err));

app.listen(SERVER_PORT, () => {
  console.log(`🚀 Zone Service running on port ${SERVER_PORT}`);
});