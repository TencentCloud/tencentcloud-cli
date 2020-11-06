**Example 1: Sample request**

>- To get the common request parameters `SecretId` and `SecretKey` (which will be used in the SDK too), please go to the [TencentCloud API Key](https://console.cloud.tencent.com/cam/capi) page.
>- Note: because of the improved security of TencentCloud API 3.0, API authentication is more complicated. You are recommended to use the Tencent Cloud SMS service with the [SDK](https://cloud.tencent.com/document/product/382/38778#SDK).

Input: 

```
tccli sms SendSms --cli-unfold-argument  \
    --PhoneNumberSet +8618511122233 +8618511122266 \
    --TemplateID 1234 \
    --Sign 'Tencent Cloud' \
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
                "SerialNo": "5000:104571066915705365784949619",
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

