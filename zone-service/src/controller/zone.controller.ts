import { Request, Response } from "express";
import zoneService from "../services/zoneService";

class ZoneController {
  async saveZone(req: Request, res: Response) {
    try {
      const zone = await zoneService.createZone(req.body);
      res.status(201).json(zone);
    } catch (error: any) {
      res.status(400).json({ message: error.message });
    }
  }
  
  async getOneZone(req: Request, res: Response) {
    try {
      const zone = await zoneService.getZoneDetails(req.params.id as string);
      res.status(200).json(zone);
    } catch (error: any) {
      res.status(404).json({ message: error.message });
    }
  }

  async updateZone(req: Request, res: Response) {
    try {
      const zone = await zoneService.updateZone(req.params.id as string, req.body);
      res.status(200).json(zone);
    } catch (error: any) {
      res.status(400).json({ message: error.message });
    }
  }

  async removeZone(req: Request, res: Response) {
    try {
      await zoneService.deleteZone(req.params.id as string);
      res.status(204).send();
    } catch (error: any) {
      res.status(400).json({ message: error.message });
    }
  }
}

export default new ZoneController();
