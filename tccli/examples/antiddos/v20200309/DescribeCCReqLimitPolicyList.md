**Example 1: 获取CC频率限制策略列表**



Input: 

```
tccli antiddos DescribeCCReqLimitPolicyList --cli-unfold-argument  \
    --Domain xx \
    --Protocol xx \
    --Business xx \
    --InstanceId xx \
    --Ip xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestLimitPolicyList": [
            {
                "Domain": "xx",
                "Protocol": "xx",
                "InstanceId": "xx",
                "Ip": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "PolicyId": "xx",
                "PolicyRecord": {
                    "ExecuteDuration": 1,
                    "Uri": "xx",
                    "Period": 1,
                    "Cookie": "xx",
                    "Mode": "xx",
                    "Action": "xx",
                    "UserAgent": "xx",
                    "RequestNum": 1
                },
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

