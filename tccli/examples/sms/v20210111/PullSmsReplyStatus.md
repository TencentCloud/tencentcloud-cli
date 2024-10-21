**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsReplyStatus --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --Limit 100
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

