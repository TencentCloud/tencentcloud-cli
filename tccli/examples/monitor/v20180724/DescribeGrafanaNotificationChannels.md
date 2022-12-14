**Example 1: 列出 Grafana 告警通道**



Input: 

```
tccli monitor DescribeGrafanaNotificationChannels --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --ChannelState 0 \
    --Limit 0 \
    --Offset 0 \
    --ChannelName test \
    --ChannelIDs nchannel-abcd1234
```

Output: 
```
{
    "Response": {
        "NotificationChannelSet": [
            {
                "ExtraOrgIds": [
                    "xx"
                ],
                "OrgIds": "xx",
                "Receivers": [
                    "xx"
                ],
                "ChannelId": "nchannel-abcd1234",
                "OrganizationIds": "xx",
                "OrgId": "xx",
                "UpdatedAt": "2020-09-22",
                "ChannelName": "xx",
                "CreatedAt": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

