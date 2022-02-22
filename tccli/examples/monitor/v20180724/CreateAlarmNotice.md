**Example 1: 创建通知模板**



Input: 

```
tccli monitor CreateAlarmNotice --cli-unfold-argument  \
    --Module monitor \
    --Name noticeA \
    --NoticeType ALL \
    --NoticeLanguage zh-CN \
    --UserNotices.0.ReceiverType USER \
    --UserNotices.0.UserIds 10001 \
    --UserNotices.0.NoticeWay SMS EMAIL \
    --UserNotices.0.StartTime 0 \
    --UserNotices.0.EndTime 1 \
    --UserNotices.0.PhoneOrder 10001 \
    --UserNotices.0.PhoneCircleInterval 60 \
    --UserNotices.0.PhoneCircleTimes 2 \
    --UserNotices.0.PhoneInnerInterval 60 \
    --UserNotices.0.NeedPhoneArriveNotice 1 \
    --UserNotices.0.PhoneCallType CIRCLE \
    --URLNotices.0.URL https://www.mytest.com/validate
```

Output: 
```
{
    "Response": {
        "NoticeId": "notice-2h92ghf2",
        "RequestId": "neh390an4opw0-45nw"
    }
}
```

