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
                "ExtraOrgIds": [
                    "xx"
                ],
                "OrgIds": "xx",
                "Receivers": [
                    "xx"
                ],
                "ChannelId": "xx",
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

