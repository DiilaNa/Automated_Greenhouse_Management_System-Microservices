import dotenv from "dotenv";
import express from "express";
import mongoose from "mongoose";
import { Eureka } from "eureka-js-client"; 

dotenv.config();

const app = express();
app.use(express.json());

const SERVER_PORT = process.env.PORT || 8081;
const MONGO_URL = process.env.MONGO_URI as string;

const client = new Eureka({
  instance: {
    app: "ZONE-SERVICE",
    hostName: "localhost",
    ipAddr: "127.0.0.1",
    statusPageUrl: `http://localhost:${SERVER_PORT}/info`,
    port: {
      $: Number(SERVER_PORT),
      "@enabled": true,
    },
    vipAddress: "ZONE-SERVICE",
    dataCenterInfo: {
      "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
      name: "MyOwn",
    },
  },
  eureka: {
    host: "localhost",
    port: 8761,
    servicePath: "/eureka/apps/",
  },
});

mongoose
  .connect(MONGO_URL)
  .then(() => {
    console.log("✅ Zone Service connected to MongoDB");

    client.start((error) => {
      if (error) {
        console.log("❌ Eureka registration failed:", error);
      } else {
        console.log("✅ Zone Service registered with Eureka successfully!");
      }
    });

    app.listen(SERVER_PORT, () => {
      console.log(`🚀 Zone Service running on port ${SERVER_PORT}`);
    });
  })
  .catch((err) => console.error("❌ MongoDB connection error:", err));
