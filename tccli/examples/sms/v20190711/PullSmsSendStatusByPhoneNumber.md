**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SendDateTime 1570526300 \
    --EndDateTime 1570526400 \
    --Offset 0 \
    --Limit 2 \
    --PhoneNumber +8615291996666 \
    --SmsSdkAppid 1400006874
```

Output: 
```
{
    "Response": {
        "PullSmsSendStatusSet": [
            {
                "Description": "DELIVRD",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "PurePhoneNumber": "+8615291996666",
                "ReportStatus": "SUCCESS",
                "UserReceiveUnixTime": 1570526317,
                "PhoneNumber": "15291996666",
                "UserReceiveTime": "2019-10-08 17:18:37",
                "NationCode": "86"
            },
            {
                "Description": "DELIVRD",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452f",
                "PurePhoneNumber": "+8615291996666",
                "ReportStatus": "SUCCESS",
                "UserReceiveUnixTime": 1570526318,
                "PhoneNumber": "15291996666",
                "UserReceiveTime": "2019-10-08 17:18:38",
                "NationCode": "86"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

