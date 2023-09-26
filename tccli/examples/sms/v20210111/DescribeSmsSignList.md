**Example 1: 请求示例**



Input: 

```
tccli sms DescribeSmsSignList --cli-unfold-argument  \
    --International 0 \
    --SignIdSet 1110 1111
```

Output: 
```
{
    "Response": {
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325",
        "DescribeSignListStatusSet": [
            {
                "SignName": "腾讯云",
                "International": 0,
                "SignId": 1110,
                "ReviewReply": "",
                "CreateTime": 1617508800,
                "StatusCode": 0
            },
            {
                "SignName": "腾讯云",
                "International": 1,
                "SignId": 1111,
                "ReviewReply": "",
                "CreateTime": 1617508801,
                "StatusCode": 0
            }
        ]
    }
}
```

