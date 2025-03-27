**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMessageList --cli-unfold-argument  \
    --InstanceId mqtt-g839agr2 \
    --Topic home \
    --StartTime 1743058422270 \
    --EndTime 1743060222270 \
    --TaskRequestId  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "DeadLetterResendSuccessTimes": 0,
                "DeadLetterResendTimes": 0,
                "Keys": "",
                "MsgId": "153970740050639FEE488932E9830036",
                "ProduceTime": "2025-03-27 15:23:35",
                "ProducerAddr": "21.57.114.216:34679",
                "Qos": "1",
                "SubTopic": "/11/",
                "Tags": "MQTT_COMMON"
            },
            {
                "DeadLetterResendSuccessTimes": 0,
                "DeadLetterResendTimes": 0,
                "Keys": "",
                "MsgId": "153970740050639FEE488932EB200037",
                "ProduceTime": "2025-03-27 15:23:35",
                "ProducerAddr": "21.57.114.216:34679",
                "Qos": "1",
                "SubTopic": "/11/",
                "Tags": "MQTT_COMMON"
            }
        ],
        "RequestId": "3381468d-6a5d-4fac-917f-726109bb968b",
        "TaskRequestId": "d43a8003-6359-4b25-a802-1ad46c98732a",
        "TotalCount": 2
    }
}
```

