**Example 1: 列出 Grafana 告警通道**



Input: 

```
tccli monitor DescribeGrafanaChannels --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --ChannelState 0 \
    --Limit 0 \
    --Offset 0 \
    --ChannelName test \
    --ChannelIds nchannel-abcd1234
```

Output: 
```
{
    "Response": {
        "NotificationChannelSet": [
            {
                "Receivers": [
                    "123"
                ],
                "ChannelId": "nchannel-abcd1234",
                "OrganizationIds": [
                    "1"
                ],
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "ChannelName": "test",
                "CreatedAt": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "requestid"
    }
}
```

