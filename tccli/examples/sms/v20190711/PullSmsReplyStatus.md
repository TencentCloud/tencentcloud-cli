**Example 1: Sample request**

>- To get the common request parameters `SecretId` and `SecretKey` (which will be used in the SDK too), please go to the [TencentCloud API Key](https://console.cloud.tencent.com/cam/capi) page.
>- Note: because of the improved security of TencentCloud API 3.0, API authentication is more complicated. You are recommended to use the Tencent Cloud SMS service with the [SDK](https://cloud.tencent.com/document/product/382/38776#SDK).

Input: 

```
tccli sms PullSmsReplyStatus --cli-unfold-argument  \
    --Limit 2\
    --SmsSdkAppid 1400006874
```

Output: 
```
{
    "Response": {
        "PullSmsReplyStatusSet": [
            {
                "ExtendCode": "11",
                "NationCode": "86",
                "PhoneNumber": "+8615291990000",
                "Sign": "Tencent Cloud",
                "ReplyContent": "xxxxx",
                "ReplyTime": "2019-10-08 17:18:36"
            },
            {
                "ExtendCode": "11",
                "NationCode": "86",
                "PhoneNumber": "+8615291990001",
                "Sign": "Tencent Cloud",
                "ReplyContent": "xxxxx",
                "ReplyTime": "2019-10-08 17:18:37"
            }
        ],
        "RequestId": "a0aabda6-cf91-4f3e-a81f-9198114a2279"
    }
}
```

