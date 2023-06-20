**Example 1: 请求示例**

请求示例

Input: 

```
tccli sms SendSms --cli-unfold-argument  \
    --PhoneNumberSet +8618511122266 +8618511122233 \
    --SmsSdkAppId 1400006666 \
    --SignName 腾讯云 \
    --TemplateId 1234 \
    --TemplateParamSet 12345 \
    --SessionContext test
```

Output: 
```
{
    "Response": {
        "SendStatusSet": [
            {
                "SerialNo": "5000:1045710669157053657849499619",
                "PhoneNumber": "+8618511122233",
                "Fee": 1,
                "SessionContext": "test",
                "Code": "Ok",
                "Message": "send success",
                "IsoCode": "CN"
            },
            {
                "SerialNo": "5000:1045710669157053657849499718",
                "PhoneNumber": "+8618511122266",
                "Fee": 1,
                "SessionContext": "test",
                "Code": "Ok",
                "Message": "send success",
                "IsoCode": "CN"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

