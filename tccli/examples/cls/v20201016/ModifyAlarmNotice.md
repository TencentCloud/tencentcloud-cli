**Example 1: 修改通知渠道组**



Input: 

```
tccli cls ModifyAlarmNotice --cli-unfold-argument  \
    --AlarmNoticeId notice-1a2c6c17-xxxx-xxxx-81be-25248ada5a4c \
    --Name zhangsan-test-copy \
    --JumpDomain https://xxxx.tent.com \
    --NoticeRules.0.NoticeReceivers.0.ReceiverType Uin \
    --NoticeRules.0.NoticeReceivers.0.ReceiverIds 11223344567 \
    --NoticeRules.0.NoticeReceivers.0.ReceiverChannels Email \
    --NoticeRules.0.NoticeReceivers.0.StartTime 01:59:59 \
    --NoticeRules.0.NoticeReceivers.0.EndTime 02:00:00 \
    --NoticeRules.0.NoticeReceivers.0.Index 0 \
    --NoticeRules.0.NoticeReceivers.0.NoticeContentId Default-zh \
    --NoticeRules.0.WebCallbacks.0.Method  \
    --NoticeRules.0.WebCallbacks.0.Url http://xxx.com \
    --NoticeRules.0.WebCallbacks.0.CallbackType WeCom \
    --NoticeRules.0.WebCallbacks.0.Body  \
    --NoticeRules.0.WebCallbacks.0.Index 1 \
    --NoticeRules.0.WebCallbacks.0.NoticeContentId Default-zh \
    --NoticeRules.0.WebCallbacks.0.WebCallbackId  \
    --NoticeRules.0.WebCallbacks.0.RemindType 0 \
    --NoticeRules.0.Type 1 \
    --NoticeRules.0.Escalate False \
    --NoticeRules.0.Interval 10 \
    --NoticeRules.0.Rule {"Value":"AND","Type":"Operation","Children":[{"Type":"Condition","Value":"NotifyType","Children":[{"Value":"In","Type":"Compare"},{"Value":"[1,2]","Type":"Value"}]}]} \
    --DeliverStatus 1 \
    --AlarmShieldStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-xxxx-xxxx-bb20-270359fb54a7"
    }
}
```

