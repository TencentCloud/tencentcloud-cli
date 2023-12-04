**Example 1: 更新 Grafana 告警通道**

更新 Grafana 告警通道

Input: 

```
tccli monitor UpdateGrafanaNotificationChannel --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --ChannelId nchannel-abcd1234 \
    --ChannelName test \
    --Receivers abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

