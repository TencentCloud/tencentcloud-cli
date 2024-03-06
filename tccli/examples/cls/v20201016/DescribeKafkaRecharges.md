**Example 1: 获取Kafka导入配置信息**

获取Kafka导入配置信息

Input: 

```
tccli cls DescribeKafkaRecharges --cli-unfold-argument  \
    --TopicId abc \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Id": "86076b49-1234-4321-ab09-a5d7e7972825",
                "TopicId": "957f4aed-1234-4321-b98b-c3c806f9e71b",
                "Name": "task-test",
                "KafkaType": 1,
                "KafkaInstance": "",
                "ServerAddr": "kafkaconsumer-ap-chongqing.aaa.com:1234",
                "IsEncryptionAddr": true,
                "Protocol": {
                    "Protocol": "sasl_plaintext",
                    "Mechanism": "PLAIN",
                    "UserName": "1234567-8146-461f-a951-348c4748f63d",
                    "Password": "AKIDxxxxx#abcdefjxxxx"
                },
                "UserKafkaTopics": "1256238147-f3061593-cd5b-4321-1234-3ba507d43301",
                "ConsumerGroupName": "",
                "Status": 1,
                "Offset": -2,
                "CreateTime": "2023-04-03 19:46:52",
                "UpdateTime": "2023-04-04 11:41:54",
                "LogRechargeRule": {
                    "RechargeType": "json_log",
                    "LogRegex": "",
                    "UnMatchLogSwitch": true,
                    "UnMatchLogKey": "LogParseFailure",
                    "UnMatchLogTimeSrc": 0,
                    "EncodingFormat": 0,
                    "DefaultTimeSwitch": true,
                    "DefaultTimeSrc": 0,
                    "TimeKey": "",
                    "TimeRegex": "",
                    "TimeFormat": "",
                    "TimeZone": "UTC-11:00",
                    "Metadata": [
                        "kafka_topic",
                        "kafka_partition",
                        "kafka_offset",
                        "kafka_timestamp"
                    ],
                    "Keys": []
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "7101f52f-a442-475b-90a3-4855133fefbf"
    }
}
```

