**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeClientEvents --cli-unfold-argument  \
    --InstanceId mqtt-pjn3nqdm \
    --StartTime 1729129907689 \
    --EndTime 1729133507689 \
    --ClientId mqttx_chongfu
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Events": [
            {
                "ClientId": "mqttx_chongfu",
                "Event": "client.subscribed",
                "Info": [
                    {
                        "Key": "topic",
                        "Value": "home/#/"
                    },
                    {
                        "Key": "qos",
                        "Value": "2"
                    },
                    {
                        "Key": "username",
                        "Value": "sun"
                    }
                ],
                "Timestamp": 1729131546478
            },
            {
                "ClientId": "mqttx_chongfu",
                "Event": "client.disconnected",
                "Info": [
                    {
                        "Key": "reason",
                        "Value": "normal"
                    },
                    {
                        "Key": "disconnected_at",
                        "Value": "1729131555468"
                    }
                ],
                "Timestamp": 1729131555468
            },
            {
                "ClientId": "mqttx_chongfu",
                "Event": "client.connected",
                "Info": [
                    {
                        "Key": "topic",
                        "Value": null
                    },
                    {
                        "Key": "qos",
                        "Value": null
                    },
                    {
                        "Key": "username",
                        "Value": "sun"
                    }
                ],
                "Timestamp": 1729131532865
            },
            {
                "ClientId": "mqttx_chongfu",
                "Event": "client.unsubscribed",
                "Info": [
                    {
                        "Key": "topic",
                        "Value": "home/#/"
                    },
                    {
                        "Key": "qos",
                        "Value": "2"
                    },
                    {
                        "Key": "username",
                        "Value": "sun"
                    }
                ],
                "Timestamp": 1729131553007
            }
        ],
        "RequestId": "6c2727c8-c012-4385-ac01-da30e2a4dff8"
    }
}
```

