package models

import "time"

type Crop struct {
	ID        uint      `gorm:"primaryKey" json:"id"`
	Name      string    `json:"name" binding:"required"`
	Variety   string    `json:"variety"`
	ZoneID    string    `json:"zoneId" binding:"required"`
	Status    string    `json:"status" gorm:"default:SEEDLING"`
	CreatedAt time.Time `json:"createdAt"`
}
