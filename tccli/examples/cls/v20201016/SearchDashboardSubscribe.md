**Example 1: 预览仪表盘订阅**

预览仪表盘订阅

Input: 

```
tccli cls SearchDashboardSubscribe --cli-unfold-argument  \
    --DashboardId xxx-xxxxxx-xxxxxx-xxxx \
    --Name 仪表盘-CLS-日报 \
    --SubscribeData.DashboardTime now-5m now \
    --SubscribeData.TemplateVariables.0.Key name \
    --SubscribeData.TemplateVariables.0.Values abc \
    --SubscribeData.NoticeModes.0.ReceiverType Uin \
    --SubscribeData.NoticeModes.0.Values 168053 \
    --SubscribeData.NoticeModes.0.ReceiverChannels Sms \
    --SubscribeData.NoticeModes.1.ReceiverType Group \
    --SubscribeData.NoticeModes.1.Values 10721522 9553840 \
    --SubscribeData.NoticeModes.1.ReceiverChannels Sms \
    --SubscribeData.NoticeModes.2.ReceiverType Email \
    --SubscribeData.NoticeModes.2.Values 3333@qq.com xxx@163.com \
    --SubscribeData.Timezone Asia/Shanghai \
    --SubscribeData.SubscribeLanguage zh \
    --SubscribeData.JumpDomain https://console.cloud.tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

