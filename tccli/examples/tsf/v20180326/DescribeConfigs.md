**Example 1: 查询配置项列表**



Input: 

```
tccli tsf DescribeConfigs --cli-unfold-argument  \
    --ConfigName test-driverapi-config \
    --ApplicationId application-jy9w6lka \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "09dd9751-6169-4db6-903c-283f89a250f2",
        "Result": {
            "TotalCount": 2,
            "Content": [
                {
                    "ConfigId": "dcfg-qab4rqwv",
                    "ConfigName": "test-driverapi-config",
                    "ConfigVersion": "v1.2.0",
                    "ConfigVersionDesc": "",
                    "ConfigValue": "logging:\r\n  config: classpath:logback-custom.xml\r\n  file: /data/logs/${spring.application.name}/root.log\r\n  level:\r\n    org.springframework.tsf: INFO\r\n    com.tencent.iov.driverapi: DEBUG\r\n    com.tencent.iov.parent: DEBUG\r\n\r\nspring:\r\n  kafka:\r\n    bootstrap-servers: 10.3.1.11:9092\r\n    producer:\r\n      retries: 0\r\n      batch-size: 16384\r\n      buffer-memory: 33554432\r\n      key-serializer: org.apache.kafka.common.serialization.StringSerializer\r\n      value-serializer: org.apache.kafka.common.s",
                    "CreationTime": "2019-04-23 11:16:26",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": "application-jy9w6lka",
                    "ApplicationName": "ruqitest_travel_driverapi",
                    "DeleteFlag": true,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-6a79b39v",
                    "ConfigName": "test-driverapi-config",
                    "ConfigVersion": "v1.2.1",
                    "ConfigVersionDesc": null,
                    "ConfigValue": "logging:\r\n  config: classpath:logback-custom.xml\r\n  file: /data/logs/${spring.application.name}/root.log\r\n  level:\r\n    org.springframework.tsf: INFO\r\n    com.tencent.iov.driverapi: DEBUG\r\n    com.tencent.iov.parent: DEBUG\r\n\r\nspring:\r\n  kafka:\r\n    bootstrap-servers: 10.3.1.11:9092\r\n    producer:\r\n      retries: 0\r\n      batch-size: 16384\r\n      buffer-memory: 33554432\r\n      key-serializer: org.apache.kafka.common.serialization.StringSerializer\r\n      value-serializer: org.apache.kafka.common.s",
                    "CreationTime": "2019-04-23 09:53:53",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": "application-jy9w6lka",
                    "ApplicationName": "ruqitest_travel_driverapi",
                    "DeleteFlag": false,
                    "ConfigType": null
                }
            ]
        }
    }
}
```

