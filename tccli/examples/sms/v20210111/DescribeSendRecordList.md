**Example 1: 请求示例**



Input: 

```
tccli sms DescribeSendRecordList --cli-unfold-argument  \
    --PhoneNumber +86136****8015 \
    --SmsSdkAppId 140***9515 \
    --BeginTime 1787850451 \
    --EndTime 1787902550 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SendRecordSet": [
            {
                "Content": "【腾讯云通信】您的验证码为0****1，5分钟内有效。",
                "IsoCode": "CN",
                "PhoneNumber": "+86136****8015",
                "RequestCode": "Ok",
                "SendStatus": 2,
                "SendTime": 1787902541,
                "SerialNo": "4719:106022169717827487984377125",
                "StatusCode": "DELIVRD",
                "UserReceiveTime": 1787902571
            }
        ],
        "TotalCount": 1,
        "RequestId": "22f73024-57b5-4f32-9657-85ef83239929"
    }
}
```

