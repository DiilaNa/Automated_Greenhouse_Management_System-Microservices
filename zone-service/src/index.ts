import dotenv from "dotenv";
import express from "express";
import router from "./routes/zone.routes";
import { eurekaClient } from "./config/server";
import { connectDB } from "./config/db";

dotenv.config();

const app = express();
app.use(express.json());

const SERVER_PORT = process.env.PORT || 8081;

connectDB();

eurekaClient.start();

app.use("/api/zones", router)

app.listen(SERVER_PORT, () => {
    console.log(`🚀 Zone Service running on port ${SERVER_PORT}`);
});
