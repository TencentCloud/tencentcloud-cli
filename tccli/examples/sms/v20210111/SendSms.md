**Example 1: 发送短信成功示例**

发送短信成功。

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

**Example 2: 发送短信失败示例**

发送短信请求中模板参数的个数与申请的模板不一致，返回发送失败。

Input: 

```
tccli sms SendSms --cli-unfold-argument  \
    --PhoneNumberSet +8618501234444 +8618501234445 \
    --SmsSdkAppId 1400006666 \
    --SignName 腾讯云 \
    --TemplateId 1110 \
    --TemplateParamSet 4370 5 \
    --SessionContext 
```

Output: 
```
{
    "Response": {
        "SendStatusSet": [
            {
                "SerialNo": "",
                "PhoneNumber": "+8618501234444",
                "Fee": 0,
                "SessionContext": "",
                "Code": "FailedOperation.TemplateParamSetNotMatchApprovedTemplate",
                "Message": "request content does not match the template content",
                "IsoCode": ""
            },
            {
                "SerialNo": "",
                "PhoneNumber": "+8618501234445",
                "Fee": 0,
                "SessionContext": "",
                "Code": "FailedOperation.TemplateParamSetNotMatchApprovedTemplat",
                "Message": "request content does not match the template content",
                "IsoCode": ""
            }
        ],
        "RequestId": "4e394811-9ebd-4d66-98ee-730b21c4a681"
    }
}
```

