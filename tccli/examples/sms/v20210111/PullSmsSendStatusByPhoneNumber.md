**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --PhoneNumber +8615291996666 \
    --BeginTime 1464624000 \
    --Offset 0 \
    --Limit 2 \
    --EndTime 1464624000
```

Output: 
```
{
    "Response": {
        "PullSmsSendStatusSet": [
            {
                "Description": "DELIVRD",
                "CountryCode": "86",
                "SubscriberNumber": "15291990000",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8615291990000",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "UserReceiveTime": 1620734188
            },
            {
                "Description": "DELIVRD",
                "CountryCode": "86",
                "SubscriberNumber": "15291990001",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8615291990001",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "UserReceiveTime": 1620734188
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

