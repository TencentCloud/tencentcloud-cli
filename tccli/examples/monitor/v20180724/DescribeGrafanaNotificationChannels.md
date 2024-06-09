**Example 1: 列出 Grafana 告警通道**

列出 Grafana 告警通道

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
                "ChannelId": "abc",
                "ChannelName": "abc",
                "Receivers": [
                    "abc"
                ],
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UpdatedAt": "2020-09-22T00:00:00+00:00",
                "OrgId": "abc",
                "ExtraOrgIds": [
                    "abc"
                ],
                "OrgIds": [
                    "abc"
                ],
                "OrganizationIds": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

