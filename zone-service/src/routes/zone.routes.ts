import { Router } from "express";
import { getAllZones } from "../controller/zone.controller";
import { authMiddleware } from "../middleware/middleware";

const router = Router();

router.get("/", authMiddleware, getAllZones);
export default router;