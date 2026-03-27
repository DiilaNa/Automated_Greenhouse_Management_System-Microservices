import zoneRepository from "../repositories/zoneRepository";
import { CreateZoneDTO, UpdateZoneDTO } from "../dto/zone.dto";

class ZoneService {
  async createZone(data: CreateZoneDTO) {
    // මෙතනදී පරීක්ෂා කරනවා දැනටමත් මේ ID එක තියෙනවද කියලා
    const existingZone = await zoneRepository.findById(data.zoneId);
    if (existingZone) {
      throw new Error("Zone ID already exists");
    }
    return await zoneRepository.save(data);
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
    return await zoneRepository.update(id, data);
  }

  async deleteZone(id: string) {
    return await zoneRepository.delete(id);
  }
}

export default new ZoneService();
