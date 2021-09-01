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
        "RequestId": "xx",
        "DescribeSignListStatusSet": [
            {
                "SignName": "xx",
                "International": 1,
                "SignId": 1,
                "ReviewReply": "xx",
                "CreateTime": 1,
                "StatusCode": 0
            },
            {
                "SignName": "xx",
                "International": 1,
                "SignId": 1,
                "ReviewReply": "xx",
                "CreateTime": 1,
                "StatusCode": 0
            }
        ]
    }
}
```

