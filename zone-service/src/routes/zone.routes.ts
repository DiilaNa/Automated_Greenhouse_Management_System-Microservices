import { Router } from "express";
import { getAllZones } from "../controller/zone.controller";

const router = Router();

router.get("/", getAllZones);
export default router;