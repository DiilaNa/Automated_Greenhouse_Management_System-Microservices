import Zone, { IZone } from "../models/Zone";
import { CreateZoneDTO, UpdateZoneDTO } from "../dto/zone.dto";

class ZoneRepository {
  async save(data: CreateZoneDTO): Promise<IZone> {
    return await Zone.create(data);
  }

  async findAll(): Promise<IZone[]> {
    return await Zone.find();
  }

  async findById(id: string): Promise<IZone | null> {
    return await Zone.findOne({ zoneId: id });
  }

  async update(id: string, data: UpdateZoneDTO): Promise<IZone | null> {
    return await Zone.findOneAndUpdate({ zoneId: id }, data, { new: true });
  }

  async delete(id: string): Promise<IZone | null> {
    return await Zone.findOneAndDelete({ zoneId: id });
  }
}

export default new ZoneRepository();
