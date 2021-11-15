**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --PhoneNumber +8615291996666 \
    --BeginTime 1620734100 \
    --Offset 0 \
    --Limit 2 \
    --EndTime 1620734200
```

Output: 
```
{
    "Response": {
        "PullSmsSendStatusSet": [
            {
                "Description": "DELIVRD",
                "CountryCode": "86",
                "SubscriberNumber": "15291996666",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8615291996666",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "UserReceiveTime": 1620734188
            },
            {
                "Description": "DELIVRD",
                "CountryCode": "86",
                "SubscriberNumber": "15291996666",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8615291996666",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e456f",
                "UserReceiveTime": 1620734188
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

