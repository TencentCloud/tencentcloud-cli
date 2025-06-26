**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeMessageDetails --cli-unfold-argument  \
    --InstanceId mqtt-g839agr2 \
    --MessageId 15397032005D639FEE4893603732005C
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Body": "this is body",
        "ClientId": "client1",
        "MessageId": "15397032005D639FEE4893603732005C",
        "OriginTopic": "home/room3",
        "Qos": "1",
        "RequestId": "ba5d5d6a-64c9-40cf-8889-21efed76389d",
        "StoreTimestamp": "1745828681259",
        "UserProperties": [
            {
                "Key": "key1",
                "Value": "value-1"
            },
            {
                "Key": "key2",
                "Value": "value-2"
            }
        ]
    }
}
```

