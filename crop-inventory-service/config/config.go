package config

type Config struct {
	DBURL        string
	EurekaServer string
	ServerPort   string
}

func LoadConfig() *Config {
	return &Config{
		DBURL:        "root:Ijse@1234@tcp(127.0.0.1:3306)/agms_crop_db?charset=utf8mb4&parseTime=True&loc=Local",
		EurekaServer: "http://localhost:8761/eureka",
		ServerPort:   ":8084",
	}
}
