package service

import (
	"github.com/hudl/fargo"
	"log"
	"time"
)

func RegisterWithEureka() {
	connection := fargo.NewConn("http://localhost:8761/eureka")

	instance := &fargo.Instance{
		HostName:       "localhost",
		App:            "CROP-INVENTORY-SERVICE",
		IPAddr:         "127.0.0.1",
		Port:           8084,
		Status:         fargo.UP,
		DataCenterInfo: fargo.DataCenterInfo{Name: fargo.MyOwn},
		LeaseInfo:      fargo.LeaseInfo{RenewalIntervalInSecs: 30},
	}

	if err := connection.RegisterInstance(instance); err != nil {
		log.Printf("⚠️ Eureka Error: %v", err)
		return
	}

	go func() {
		for {
			connection.HeartBeatInstance(instance)
			time.Sleep(30 * time.Second)
		}
	}()
	log.Println("🚀 Registered with Eureka Dashboard!")
}
