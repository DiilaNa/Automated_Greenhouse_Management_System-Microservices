package main

import (
	"crop-inventory-service/config"
	"crop-inventory-service/controller"
	"crop-inventory-service/repository"
	"crop-inventory-service/service"
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("🚀 Service is starting...")
	cfg := config.LoadConfig()

	repository.InitDB(cfg.DBURL)

	service.RegisterWithEureka()

	r := gin.Default()
	cropRoutes := r.Group("/api/crops")
	{
		cropRoutes.POST("/save", controllers.RegisterCrop)
		cropRoutes.PUT("/:id/status", controllers.UpdateCropStatus)
		cropRoutes.GET("getAll", controllers.GetAllCrops)
	}

	log.Printf("🚀 Server starting on %s", cfg.ServerPort)
	if err := r.Run(cfg.ServerPort); err != nil {
		log.Fatal("❌ Failed to start server: ", err)
	}
}
