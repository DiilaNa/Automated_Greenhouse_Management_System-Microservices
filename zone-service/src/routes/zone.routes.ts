import { Router } from "express";
import { authMiddleware } from "../middleware/middleware";
import zoneController from "../controller/zone.controller";

const router = Router();

router.post("/saveZone", zoneController.saveZone);
router.get("/getAllZones", authMiddleware, zoneController.getZones);
router.get("/getZoneDetails/:id", authMiddleware, zoneController.getOneZone);
router.put("/updateZone/:id", authMiddleware, zoneController.updateZone);
router.delete("/deleteZone/:id", authMiddleware, zoneController.removeZone);

export default router;