**Example 1: 创建通知渠道组（简易模式）**

包含两个通知渠道：
* 使用短信（sms）、电话（phone）通知用户组（Group），用户组id为27411
* 发送通知至企业微信（WeCom）机器人

Input: 

```
tccli cls CreateAlarmNotice --cli-unfold-argument  \
    --Name demoAlarmNotice1 \
    --Type All \
    --NoticeReceivers.0.ReceiverType Group \
    --NoticeReceivers.0.ReceiverIds 27411 \
    --NoticeReceivers.0.ReceiverChannels Sms Phone \
    --NoticeReceivers.0.StartTime 00:00:00 \
    --NoticeReceivers.0.EndTime 23:59:59 \
    --NoticeReceivers.0.NoticeContentId Default-zh \
    --NoticeReceivers.0.Index 1 \
    --WebCallbacks.0.Method POST \
    --WebCallbacks.0.CallbackType WeCom \
    --WebCallbacks.0.NoticeContentId Default-zh \
    --WebCallbacks.0.Url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxx-xxxx \
    --DeliverStatus 1 \
    --AlarmShieldStatus 2
```

Output: 
```
{
    "Response": {
        "AlarmNoticeId": "notice-b44d3a04-xxxx-4f9d-91f8-8abab903d885",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

**Example 2: 创建通知渠道组（高级模式）**

包含两个环节，告警先通知环节1，10分钟后如果告警无人认领且未恢复时通知环节2.
环节1包含2个通知渠道：
* 使用短信（sms）、电话（phone）通知用户组（Group），用户组id为27411
* 发送通知至企业微信（WeCom）机器人
环节2包含1个通知渠道
* 使用短信（sms）、电话（phone）通知用户组（Uin），用户id为6318337

Input: 

```
tccli cls CreateAlarmNotice --cli-unfold-argument  \
    --Name demoAlarmNotice2 \
    --NoticeRules.0.NoticeReceivers.0.ReceiverType Group \
    --NoticeRules.0.NoticeReceivers.0.ReceiverIds 27411 \
    --NoticeRules.0.NoticeReceivers.0.ReceiverChannels Sms Phone \
    --NoticeRules.0.NoticeReceivers.0.StartTime 00:00:00 \
    --NoticeRules.0.NoticeReceivers.0.EndTime 23:59:59 \
    --NoticeRules.0.NoticeReceivers.0.NoticeContentId Default-zh \
    --NoticeRules.0.WebCallbacks.0.Method POST \
    --NoticeRules.0.WebCallbacks.0.CallbackType WeCom \
    --NoticeRules.0.WebCallbacks.0.NoticeContentId Default-zh \
    --NoticeRules.0.WebCallbacks.0.Url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxx-xxxx \
    --NoticeRules.0.Escalate True \
    --NoticeRules.0.Type 1 \
    --NoticeRules.0.Interval 10 \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.ReceiverType Uin \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.ReceiverIds 6318337 \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.ReceiverChannels Sms Phone \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.StartTime 00:00:00 \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.EndTime 23:59:59 \
    --NoticeRules.0.EscalateNotice.NoticeReceivers.0.NoticeContentId Default-zh \
    --NoticeRules.0.EscalateNotice.Escalate False \
    --NoticeRules.0.Rule {"Value":"AND","Type":"Operation","Children":[{"Type":"Condition","Value":"NotifyType","Children":[{"Value":"In","Type":"Compare"},{"Value":"[1,2]","Type":"Value"}]}]} \
    --DeliverStatus 1 \
    --AlarmShieldStatus 2
```

Output: 
```
{
    "Response": {
        "AlarmNoticeId": "notice-b44d3a04-xxxx-4f9d-91f8-8abab903d885",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

