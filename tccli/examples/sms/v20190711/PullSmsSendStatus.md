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
                "UserReceiveUnixTime": 1,
                "NationCode": "86",
                "PurePhoneNumber": "+8615291996666",
                "PhoneNumber": "15291996666",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            },
            {
                "UserReceiveTime": "2019-10-08 17:18:37",
                "UserReceiveUnixTime": 1,
                "NationCode": "86",
                "PurePhoneNumber": "+8615291997777",
                "PhoneNumber": "15291997777",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e552f",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

