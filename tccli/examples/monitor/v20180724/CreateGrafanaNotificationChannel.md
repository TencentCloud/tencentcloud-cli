**Example 1: 创建 Grafana 告警通道**

创建 Grafana 告警通道

Input: 

```
tccli monitor CreateGrafanaNotificationChannel --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --ChannelName test \
    --OrgId 0 \
    --Receivers notice-7k7q3qzr
```

Output: 
```
{
    "Response": {
        "ChannelId": "99434792",
        "RequestId": "e3adaaf0-7266-4949-be41-bed713136876"
    }
}
```

