**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatus --cli-unfold-argument  \
    --Limit 2 \
    --SmsSdkAppid 1400006874
```

Output: 
```
{
    "Response": {
        "PullSmsSendStatusSet": [
            {
                "UserReceiveTime": "2019-10-08 17:18:37",
                "UserReceiveUnixTime": 1570526317,
                "NationCode": "86",
                "PurePhoneNumber": "+8618501234444",
                "PhoneNumber": "18501234444",
                "SerialNo": "5000:1045710669157053657849499619",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            },
            {
                "UserReceiveTime": "2019-10-08 17:18:37",
                "UserReceiveUnixTime": 1570526317,
                "NationCode": "86",
                "PurePhoneNumber": "+8618501234445",
                "PhoneNumber": "18501234445",
                "SerialNo": "5000:1045710669157053657849499718",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

