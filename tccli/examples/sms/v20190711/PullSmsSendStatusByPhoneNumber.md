**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SendDateTime 1570526300 \
    --EndDateTime 1570526400 \
    --Offset 0 \
    --Limit 2 \
    --PhoneNumber +8618501234444 \
    --SmsSdkAppid 1400006666
```

Output: 
```
{
    "Response": {
        "PullSmsSendStatusSet": [
            {
                "Description": "DELIVRD",
                "SerialNo": "5000:1045710669157053657849499619",
                "PurePhoneNumber": "+8618501234444",
                "ReportStatus": "SUCCESS",
                "UserReceiveUnixTime": 1570526317,
                "PhoneNumber": "18501234444",
                "UserReceiveTime": "2019-10-08 17:18:37",
                "NationCode": "86"
            },
            {
                "Description": "DELIVRD",
                "SerialNo": "5000:1045710669157053657849498556",
                "PurePhoneNumber": "+8618501234444",
                "ReportStatus": "SUCCESS",
                "UserReceiveUnixTime": 1570526318,
                "PhoneNumber": "18501234444",
                "UserReceiveTime": "2019-10-08 17:18:38",
                "NationCode": "86"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

