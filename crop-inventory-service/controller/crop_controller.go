package controllers

import (
	"crop-inventory-service/models"
	"crop-inventory-service/repository"
	"github.com/gin-gonic/gin"
	"net/http"
)

func RegisterCrop(c *gin.Context) {
	var crop models.Crop
	if err := c.ShouldBindJSON(&crop); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	repository.DB.Create(&crop)
	c.JSON(http.StatusCreated, crop)
}

func GetAllCrops(c *gin.Context) {
	var crops []models.Crop
	repository.DB.Find(&crops)
	c.JSON(http.StatusOK, gin.H{"inventory": crops})
}

func UpdateCropStatus(c *gin.Context) {
	id := c.Param("id")
	var input struct {
		Status string `json:"status" binding:"required"`
	}

	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Status is required"})
		return
	}

	var crop models.Crop
	if err := repository.DB.First(&crop, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Crop not found"})
		return
	}

	repository.DB.Model(&crop).Update("Status", input.Status)
	c.JSON(http.StatusOK, crop)
}
