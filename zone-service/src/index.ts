import dotenv from "dotenv";
import express from "express";
import mongoose from "mongoose";
import { Eureka } from "eureka-js-client"; 
import router from "./routes/zone.routes";
import { eurekaClient } from "./config/server";
import { connectDB } from "./config/db";

dotenv.config();

const app = express();
app.use(express.json());

const SERVER_PORT = process.env.PORT || 8081;

connectDB();

eurekaClient.start();

app.use("/api/v1/zone", router)

app.listen(SERVER_PORT, () => {
    console.log(`🚀 Zone Service running on port ${SERVER_PORT}`);
});
