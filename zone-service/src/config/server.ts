import { Eureka } from "eureka-js-client";

export const eurekaClient = new Eureka({
  instance: {
    app: "ZONE-SERVICE",
    hostName: "localhost",
    ipAddr: "127.0.0.1",
    port: { $: 8081, "@enabled": true },
    vipAddress: "ZONE-SERVICE",
    dataCenterInfo: {
      "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
      name: "MyOwn",
    },
  },
  eureka: {
    host: "localhost",
    port: 8761,
    servicePath: "/eureka/apps/",
  },
});
