**Example 1: 请求示例**

请求示例

Input: 

```
tccli sms SendSms --cli-unfold-argument  \
    --PhoneNumberSet +8618511122233 +8618511122266 \
    --TemplateID 1234 \
    --Sign 腾讯云 \
    --TemplateParamSet 12345 \
    --SmsSdkAppid 1400006666 \
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
                "SerialNo": "5000:104571066915705365784949619",
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

