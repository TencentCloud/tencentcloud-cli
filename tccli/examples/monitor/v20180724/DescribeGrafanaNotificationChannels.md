**Example 1: 列出 Grafana 告警通道**

列出 Grafana 告警通道

Input: 

```
tccli monitor DescribeGrafanaNotificationChannels --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --ChannelState 0 \
    --Limit 0 \
    --Offset 0 \
    --ChannelName alert-test \
    --ChannelIDs nchannel-abcd1234
```

Output: 
```
{
    "Response": {
        "NotificationChannelSet": [
            {
                "ChannelId": "nchannel-xxxxxxxx",
                "ChannelName": "alert-test",
                "CreatedAt": "2026-06-11T12:01:31+08:00",
                "OrgId": "1",
                "ExtraOrgIds": null,
                "OrgIds": [
                    "1"
                ],
                "OrganizationIds": [
                    "1"
                ],
                "Receivers": [
                    "Consumer-xxxxxxxx"
                ],
                "UpdatedAt": "2026-06-11T12:01:31+08:00"
            }
        ],
        "RequestId": "6f4848cc-95cd-4385-88aa-be47fb64974d"
    }
}
```

