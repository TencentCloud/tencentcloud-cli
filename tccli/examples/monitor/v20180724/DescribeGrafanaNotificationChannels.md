**Example 1: 列出 Grafana 告警通道**



Input: 

```
tccli monitor DescribeGrafanaNotificationChannels --cli-unfold-argument  \
    --InstanceId xx \
    --ChannelState 0 \
    --Limit 0 \
    --Offset 0 \
    --ChannelName xx \
    --ChannelIDs xx
```

Output: 
```
{
    "Response": {
        "NotificationChannelSet": [
            {
                "ChannelId": "xx",
                "UpdatedAt": "2020-09-22",
                "ChannelName": "xx",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "Receivers": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

