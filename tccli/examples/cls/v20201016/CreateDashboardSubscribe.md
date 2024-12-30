**Example 1: 创建仪表盘订阅**

创建仪表盘订阅

Input: 

```
tccli cls CreateDashboardSubscribe --cli-unfold-argument  \
    --Name 每月最后一天早晨10点 \
    --DashboardId dashboard-0d954d68-xxxx-xxxx-95a6-f9eff0db370f \
    --Cron 0 40 20 * * ? \
    --SubscribeData.DashboardTime 2022-05-01T00:00:00.000 2022-05-31T23:59:59.999 \
    --SubscribeData.TemplateVariables.0.Key name \
    --SubscribeData.TemplateVariables.0.Values zhangsan \
    --SubscribeData.NoticeModes.0.ReceiverType Uin \
    --SubscribeData.NoticeModes.0.Values 168053 \
    --SubscribeData.NoticeModes.0.ReceiverChannels Sms \
    --SubscribeData.NoticeModes.1.ReceiverType Group \
    --SubscribeData.NoticeModes.1.Values 10721522 9553840 \
    --SubscribeData.NoticeModes.1.ReceiverChannels Sms \
    --SubscribeData.NoticeModes.2.ReceiverType Email \
    --SubscribeData.NoticeModes.2.Values 3333@qq.com xxx@163.com
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-xxxx-xxxx-bb20-270359fb54a7"
    }
}
```

