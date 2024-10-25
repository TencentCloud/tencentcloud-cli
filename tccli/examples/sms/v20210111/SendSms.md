**Example 1: 请求示例**



Input: 

```
tccli sms SendSms --cli-unfold-argument  \
    --PhoneNumberSet +8618501234444 +8618501234445 \
    --SmsSdkAppId 1400006666 \
    --SignName 腾讯云 \
    --TemplateId 1110 \
    --TemplateParamSet 4370 \
    --SessionContext outsid_1729495320_1011
```

Output: 
```
{
    "Response": {
        "SendStatusSet": [
            {
                "SerialNo": "5000:1045710669157053657849499619",
                "PhoneNumber": "+8618501234444",
                "Fee": 1,
                "SessionContext": "outsid_1729495320_1011",
                "Code": "Ok",
                "Message": "send success",
                "IsoCode": "CN"
            },
            {
                "SerialNo": "5000:1045710669157053657849499718",
                "PhoneNumber": "+8618501234445",
                "Fee": 1,
                "SessionContext": "outsid_1729495320_1011",
                "Code": "Ok",
                "Message": "send success",
                "IsoCode": "CN"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

