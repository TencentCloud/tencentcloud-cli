**Example 1: 获取Kafka导入配置信息**

获取Kafka导入配置信息

Input: 

```
tccli cls DescribeKafkaRecharges --cli-unfold-argument  \
    --TopicId c8e26faa-xxxx-xxxx-xxxx-5d941d3a57d1 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "ConsumerGroupName": "test1",
                "CreateTime": "2024-01-24 15:00:06",
                "Id": "f574db7d-xxxx-xxxx-8a04-35f7fe71a4d0",
                "IsEncryptionAddr": true,
                "KafkaInstance": "",
                "KafkaType": 1,
                "LogRechargeRule": {
                    "DefaultTimeSrc": 0,
                    "DefaultTimeSwitch": true,
                    "EncodingFormat": 0,
                    "Keys": [],
                    "LogRegex": "",
                    "Metadata": [
                        "kafka_topic",
                        "kafka_partition",
                        "kafka_offset",
                        "kafka_timestamp"
                    ],
                    "RechargeType": "json_log",
                    "TimeFormat": "",
                    "TimeKey": "",
                    "TimeRegex": "",
                    "TimeZone": "UTC+08:00",
                    "UnMatchLogKey": "LogParseFailure",
                    "UnMatchLogSwitch": true,
                    "UnMatchLogTimeSrc": 0
                },
                "Name": "kafkaRechargeTest1",
                "Offset": -2,
                "Protocol": {
                    "Mechanism": "PLAIN",
                    "Password": "Axxxxxx#lFSOxxxxxx",
                    "Protocol": "sasl_plaintext",
                    "UserName": "05593101-xxxx-xxxx-8a71-44f8340e1327"
                },
                "ServerAddr": "kafka-xxxx.com:8050",
                "Status": 1,
                "TopicId": "c8e26faa-xxxx-xxxx-ad8c-5d941d3a57d1",
                "UpdateTime": "2024-07-30 15:07:36",
                "UserKafkaTopics": "1254077820-9fc67c9d-xxxx-xxxx-b836-c6520b7393cc"
            }
        ],
        "RequestId": "de82c8c5-xxxx-xxxx-8f44-ec6bd80d7b6d",
        "TotalCount": 1
    }
}
```

