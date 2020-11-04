**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsReplyStatus --cli-unfold-argument  \
    --Limit 2\
    --SmsSdkAppid 1400006874
```

Output: 
```
{
    "Response": {
        "PullSmsReplyStatusSet": [
            {
                "ExtendCode": "11",
                "NationCode": "86",
                "PhoneNumber": "+8615291990000",
                "Sign": "腾讯云",
                "ReplyContent": "xxxxx",
                "ReplyTime": "2019-10-08 17:18:36"
            },
            {
                "ExtendCode": "11",
                "NationCode": "86",
                "PhoneNumber": "+8615291990001",
                "Sign": "腾讯云",
                "ReplyContent": "xxxxx",
                "ReplyTime": "2019-10-08 17:18:37"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

