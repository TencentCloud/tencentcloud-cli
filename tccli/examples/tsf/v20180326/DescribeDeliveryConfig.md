**Example 1: 获取单个投递项配置**



Input: 

```
tccli tsf DescribeDeliveryConfig --cli-unfold-argument  \
    --ConfigId config-kl29sh7n
```

Output: 
```
{
    "Response": {
        "RequestId": "00b0009f-80ad-41fd-8bb8-f430d12f3911",
        "Result": {
            "CollectPath": [
                ""
            ],
            "ConfigId": "send-data-to-kafka-nalj8bgy",
            "ConfigName": "rtest222",
            "CustomRule": null,
            "EnableAuth": false,
            "EnableGlobalLineRule": false,
            "KafkaAddress": null,
            "KafkaInfos": [
                {
                    "CustomRule": "",
                    "LineRule": "",
                    "Path": [
                        "/test/1.log"
                    ],
                    "Topic": "test"
                }
            ],
            "KafkaVIp": "127.0.1:9200",
            "KafkaVPort": null,
            "LineRule": "default",
            "Password": null,
            "Topic": "",
            "Username": null
        }
    }
}
```

