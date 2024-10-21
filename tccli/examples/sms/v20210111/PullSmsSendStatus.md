**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatus --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
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
                "SubscriberNumber": "18501234445",
                "ReportStatus": "SUCCESS",
                "PhoneNumber": "+8618501234445",
                "SerialNo": "5000:1045710669157053657849499718",
                "UserReceiveTime": 1620734188,
                "SessionContext": ""
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

