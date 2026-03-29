package repository

import (
	"crop-inventory-service/models"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"log"
)

var DB *gorm.DB

func InitDB(dsn string) {
	var err error
	DB, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("❌ Failed to connect to MySQL:", err)
	}
	DB.AutoMigrate(&models.Crop{})
	log.Println("✅ MySQL Connected & Migrated!")
}
