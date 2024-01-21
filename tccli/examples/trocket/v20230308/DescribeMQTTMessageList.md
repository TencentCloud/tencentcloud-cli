**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTMessageList --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --Topic topic24 \
    --Offset 0 \
    --Limit 20 \
    --StartTime 1705373755266 \
    --EndTime 1705632955266 \
    --TaskRequestId  
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "DeadLetterResendSuccessTimes": null,
                "DeadLetterResendTimes": null,
                "Keys": null,
                "MsgId": "0B8D67F0002D6ACBCFC0557BCEBA0001",
                "ProduceTime": "2024-01-17 14:22:57",
                "ProducerAddr": "11.176.16.153:51134",
                "Qos": "1",
                "SubTopic": "/1/",
                "Tags": "MQTT_COMMON"
            },
            {
                "DeadLetterResendSuccessTimes": null,
                "DeadLetterResendTimes": null,
                "Keys": null,
                "MsgId": "0B8D67F0002D6ACBCFC0557B1A980000",
                "ProduceTime": "2024-01-17 14:22:11",
                "ProducerAddr": "11.176.16.153:44044",
                "Qos": "0",
                "SubTopic": "",
                "Tags": "MQTT_COMMON"
            }
        ],
        "RequestId": "116cd3f5-668f-42fe-8572-fcd5d3a31377",
        "TaskRequestId": "e3d14393-4701-4f62-8a7d-b52bd59b5ace",
        "TotalCount": 2
    }
}
```

