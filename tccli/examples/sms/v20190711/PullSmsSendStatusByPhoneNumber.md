**Example 1: Sample request**

>- To get the common request parameters `SecretId` and `SecretKey` (which will be used in the SDK too), please go to the [TencentCloud API Key](https://console.cloud.tencent.com/cam/capi) page.
>- Note: because of the improved security of TencentCloud API 3.0, API authentication is more complicated. You are recommended to use the Tencent Cloud SMS service with the [SDK](https://cloud.tencent.com/document/product/382/38773#SDK).

Input: 

```
tccli sms PullSmsSendStatusByPhoneNumber --cli-unfold-argument  \
    --SendDateTime 1464624000 \
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

