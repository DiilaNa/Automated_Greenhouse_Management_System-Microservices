import { Router } from "express";
import zoneController from "../controller/zone.controller";

const router = Router();

router.post("/saveZone", zoneController.saveZone);
router.get("/getZoneDetails/:id", zoneController.getOneZone);
router.put("/updateZone/:id", zoneController.updateZone);
router.delete("/deleteZone/:id", zoneController.removeZone);

export default router;