**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsReplyStatus --cli-unfold-argument  \
    --Limit 2 \
    --SmsSdkAppid 1400006874
```

Output: 
```
{
    "Response": {
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279",
        "PullSmsReplyStatusSet": [
            {
                "ReplyContent": "xxxxxx",
                "ReplyUnixTime": 1620734188,
                "ExtendCode": "11",
                "ReplyTime": "2021-05-11 19:56:28",
                "Sign": "腾讯云",
                "PhoneNumber": "+8615291990000",
                "NationCode": "86"
            },
            {
                "ReplyContent": "xxxxxx",
                "ReplyUnixTime": 1620734189,
                "ExtendCode": "11",
                "ReplyTime": "2021-05-11 19:56:29",
                "Sign": "腾讯云",
                "PhoneNumber": "+8615291990001",
                "NationCode": "86"
            }
        ]
    }
}
```

