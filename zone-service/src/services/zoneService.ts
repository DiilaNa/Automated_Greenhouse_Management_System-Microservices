import axios from "axios";
import zoneRepository from "../repositories/zoneRepository";
import { CreateZoneDTO, UpdateZoneDTO } from "../dto/zone.dto";

class ZoneService {
  private readonly EXTERNAL_API_BASE_URL = "http://104.211.95.241:8080/api";

  async createZone(data: CreateZoneDTO,token:string) {
    if (data.minTemp >= data.maxTemp) {
      throw new Error("Validation Error: minTemp must be strictly less than maxTemp");
    }

    const existingZone = await zoneRepository.findById(data.zoneId);
    if (existingZone) {
      throw new Error("Zone ID already exists");
    }

    try {
      console.log(`Registering device for Zone: ${data.zoneId}...`);

      const iotResponse = await axios.post(
          `${this.EXTERNAL_API_BASE_URL}/devices`,
          {
            name: `${data.zoneName}-Sensor`,
            zoneId: data.zoneId,
          },
          {
            headers: { Authorization: token }
          }
      );

      const realDeviceId = iotResponse.data.deviceId;

      const finalData: any = {
        ...data,
        deviceId: realDeviceId,
      };

      return await zoneRepository.save(finalData);

    } catch (error: any) {
      console.error("IoT Service Integration Error:", error.response?.data || error.message);
      throw new Error("IoT Registration Failed. Zone creation aborted.");
    }
  }

  async getAllZones() {
    return await zoneRepository.findAll();
  }
  async getZoneDetails(id: string) {
    const zone = await zoneRepository.findById(id);
    if (!zone) throw new Error("Zone not found");
    return zone;
  }

  async updateZone(id: string, data: UpdateZoneDTO) {
    if (data.minTemp !== undefined && data.maxTemp !== undefined) {
      if (data.minTemp >= data.maxTemp) {
        throw new Error("Validation Error: minTemp must be strictly less than maxTemp");
      }
    }

    return await zoneRepository.update(id, data);
  }

  async deleteZone(id: string) {
    return await zoneRepository.delete(id);
  }
}

export default new ZoneService();