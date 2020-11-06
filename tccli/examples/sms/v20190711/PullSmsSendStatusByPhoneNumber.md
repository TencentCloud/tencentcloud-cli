**Example 1: 请求示例**



Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SendDateTime 1464624000 \
    --EndDateTime 1464624123 \
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
                "UserReceiveTime": "2019-10-08 17:18:37",
                "NationCode": "86",
                "PurePhoneNumber": "+8615291996666",
                "PhoneNumber": "15291996666",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            },
            {
                "UserReceiveTime": "2019-10-08 17:18:37",
                "NationCode": "86",
                "PurePhoneNumber": "+8615291996666",
                "PhoneNumber": "15291996666",
                "SerialNo": "14:19325917feb3914eb78b50d6182d7e452e",
                "ReportStatus": "SUCCESS",
                "Description": "DELIVRD"
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

