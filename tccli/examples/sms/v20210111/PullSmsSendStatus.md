**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatus --cli-unfold-argument  \
    --SmsSdkAppId 1400006874 \
    --Limit 100
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
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e462f",
                "UserReceiveTime": 1620734188
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

