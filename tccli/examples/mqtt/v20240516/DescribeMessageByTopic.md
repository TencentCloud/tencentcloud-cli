**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeMessageByTopic --cli-unfold-argument  \
    --InstanceId mqtt-g839agr2 \
    --Topic home/room3 \
    --StartTime 1745828681259
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ClientId": "mqttxxxxxx",
                "MessageId": "15397032005D639FEE48935F932F004D",
                "OriginTopic": "home/room3",
                "Qos": "1",
                "StoreTimestamp": "2025-04-29 14:48:34"
            },
            {
                "ClientId": "mqttxxxxxx",
                "MessageId": "15397032005D639FEE48935FA6B80050",
                "OriginTopic": "home/room3",
                "Qos": "1",
                "StoreTimestamp": "2025-04-29 14:48:39"
            },
            {
                "ClientId": "mqttxxxxxx",
                "MessageId": "15397032005D639FEE48935FBA410057",
                "OriginTopic": "home/room3",
                "Qos": "1",
                "StoreTimestamp": "2025-04-29 14:48:44"
            },
            {
                "ClientId": "mqttxxxxxx",
                "MessageId": "15397032005D639FEE4893603732005C",
                "OriginTopic": "home/room3",
                "Qos": "1",
                "StoreTimestamp": "2025-04-29 14:49:16"
            }
        ],
        "RequestId": "6af56edc-5085-4583-8366-7f125c973603"
    }
}
```

