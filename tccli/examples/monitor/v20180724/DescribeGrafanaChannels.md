**Example 1: 列出 Grafana 告警通道**



Input: 

```
tccli monitor DescribeGrafanaChannels --cli-unfold-argument  \
    --InstanceId xx \
    --ChannelState 0 \
    --Limit 0 \
    --Offset 0 \
    --ChannelName xx \
    --ChannelIds xx
```

Output: 
```
{
    "Response": {
        "NotificationChannelSet": [
            {
                "Receivers": [
                    "xx"
                ],
                "ChannelId": "xx",
                "OrganizationIds": [
                    "xx"
                ],
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "ChannelName": "xx",
                "CreatedAt": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

