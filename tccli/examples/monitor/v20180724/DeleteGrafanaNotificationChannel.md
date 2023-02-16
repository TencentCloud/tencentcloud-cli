**Example 1: 删除 Grafana 告警通道**

删除 Grafana 告警通道

Input: 

```
tccli monitor DeleteGrafanaNotificationChannel --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --ChannelIDs nchannel-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

