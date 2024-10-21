**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --PhoneNumber +8618501234444 \
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
                "SubscriberNumber": "18501234444",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8618501234444",
                "SerialNo": "5000:1045710669157053657849499619",
                "UserReceiveTime": 1620734188,
                "SessionContext": ""
            },
            {
                "Description": "DELIVRD",
                "CountryCode": "86",
                "SubscriberNumber": "18501234444",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8618501234444",
                "SerialNo": "5000:1045710669157053657849498556",
                "UserReceiveTime": 1620734188,
                "SessionContext": ""
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

