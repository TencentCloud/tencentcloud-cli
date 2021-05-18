**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsReplyStatus --cli-unfold-argument  \
    --SmsSdkAppId 1400006874 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279",
        "PullSmsReplyStatusSet": [
            {
                "CountryCode": "86",
                "ReplyContent": "xxxxxx",
                "SubscriberNumber": "15291990000",
                "ExtendCode": "11",
                "ReplyTime": 1620734188,
                "PhoneNumber": "+8615291990000",
                "SignName": "腾讯云"
            },
            {
                "CountryCode": "86",
                "ReplyContent": "xxxxxx",
                "SubscriberNumber": "15291990001",
                "ExtendCode": "11",
                "ReplyTime": 1620734189,
                "PhoneNumber": "+8615291990001",
                "SignName": "腾讯云"
            }
        ]
    }
}
```

