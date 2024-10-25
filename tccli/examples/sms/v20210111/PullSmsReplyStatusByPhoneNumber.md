**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsReplyStatusByPhoneNumber --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --PhoneNumber +8618501234444 \
    --BeginTime 1620734100 \
    --Offset 0 \
    --Limit 2 \
    --EndTime 1620734200
```

Output: 
```
{
    "Response": {
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279",
        "PullSmsReplyStatusSet": [
            {
                "CountryCode": "86",
                "ReplyContent": "1",
                "SubscriberNumber": "18501234444",
                "ExtendCode": "11",
                "ReplyTime": 1620734188,
                "PhoneNumber": "+8618501234444",
                "SignName": "腾讯云"
            },
            {
                "CountryCode": "86",
                "ReplyContent": "2",
                "SubscriberNumber": "18501234444",
                "ExtendCode": "11",
                "ReplyTime": 1620734189,
                "PhoneNumber": "+8618501234444",
                "SignName": "腾讯云"
            }
        ]
    }
}
```

