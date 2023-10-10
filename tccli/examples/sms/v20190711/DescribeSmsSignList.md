**Example 1: 请求示例**



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
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325",
        "DescribeSignListStatusSet": [
            {
                "SignName": "腾讯云",
                "International": 1,
                "SignId": 1,
                "ReviewReply": "",
                "CreateTime": 1,
                "StatusCode": 0
            },
            {
                "SignName": "Tencent",
                "International": 1,
                "SignId": 1,
                "ReviewReply": "",
                "CreateTime": 1,
                "StatusCode": 0
            }
        ]
    }
}
```

