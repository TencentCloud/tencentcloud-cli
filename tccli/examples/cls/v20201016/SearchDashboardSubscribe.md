**Example 1: 预览仪表盘订阅**

预览仪表盘订阅

Input: 

```
tccli cls SearchDashboardSubscribe --cli-unfold-argument  \
    --Name 订阅任务-oss大盘-2023-02-28_10:19 \
    --DashboardId dashboard-0d954d68-xxxx-xxxx-95a6-f9eff0db370f \
    --SubscribeData.DashboardTime now-d now \
    --SubscribeData.NoticeModes.0.ReceiverType Uin \
    --SubscribeData.NoticeModes.0.ReceiverChannels Email \
    --SubscribeData.NoticeModes.0.Values 11223344123 \
    --SubscribeData.JumpDomain https://xxx.tent.com \
    --SubscribeData.SubscribeLanguage zh \
    --SubscribeData.Timezone Asia/Shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-xxxx-xxxx-bb20-270359fb54a7"
    }
}
```

