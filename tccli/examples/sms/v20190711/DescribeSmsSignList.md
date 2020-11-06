**Example 1: Sample request**

>- To get the common request parameters `SecretId` and `SecretKey` (which will be used in the SDK too), please go to the [TencentCloud API Key](https://console.cloud.tencent.com/cam/capi) page.
>- Note: because of the improved security of TencentCloud API 3.0, API authentication is more complicated. You are recommended to use the Tencent Cloud SMS service with the [SDK](https://cloud.tencent.com/document/product/382/41429#SDK).

Input: 

```
tccli sms DescribeSmsSignList --cli-unfold-argument  \
    --SignIdSet 1110 1111 \
    --International 0
```

Output: 
```
{
    "Response": {
        "DescribeSignListStatusSet": [
            {
                "SignId": 1110,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "SignName": "xxx",
                "CreateTime": "2020-01-13 15:18:20"
            },
            {
                "SignId": 1111,
                "International": 0,
                "StatusCode": 0,
                "ReviewReply": "xxx",
                "SignName": "xxx",
                "CreateTime": "2020-01-13 15:18:21"
            }
        ],
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

