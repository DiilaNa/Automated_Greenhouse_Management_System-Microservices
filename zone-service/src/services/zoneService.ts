import axios from "axios";
import zoneRepository from "../repositories/zoneRepository";
import { CreateZoneDTO, UpdateZoneDTO } from "../dto/zone.dto";

class ZoneService {
  async createZone(data: CreateZoneDTO) {
    if (data.minTemp >= data.maxTemp) {
      throw new Error(
        "Validation Error: minTemp must be strictly less than maxTemp",
      );
    }

    const existingZone = await zoneRepository.findById(data.zoneId);
    if (existingZone) {
      throw new Error("Zone ID already exists");
    }

    try {
      // const iotResponse = await axios.post(
      //   "http://localhost:8082/api/devices/register",
      //   {
      //     zoneId: data.zoneId,
      //   },
      // );

      const finalData: any = {
        ...data,
        deviceId: "dev-001", 
      };

      return await zoneRepository.save(finalData);
    } catch (error: any) {
      console.error("IoT Service Integration Error:", error.message);
      throw new Error("IoT Registration Failed. Zone creation aborted.");
    }
  }

  async getZoneDetails(id: string) {
    const zone = await zoneRepository.findById(id);
    if (!zone) throw new Error("Zone not found");
    return zone;
  }

  async updateZone(id: string, data: UpdateZoneDTO) {
    if (data.minTemp && data.maxTemp && data.minTemp >= data.maxTemp) {
      throw new Error(
        "Validation Error: minTemp must be strictly less than maxTemp",
      );
    }
    return await zoneRepository.update(id, data);
  }

  async deleteZone(id: string) {
    return await zoneRepository.delete(id);
  }
}

export default new ZoneService();
