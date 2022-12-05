**Example 1: 获取CC频率限制策略列表**



Input: 

```
tccli antiddos DescribeCCReqLimitPolicyList --cli-unfold-argument  \
    --Business bgp-multip \
    --InstanceId bgp-00000001 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ea775a73-7de5-4d36-aca0-29307e7c4f27",
        "Total": 1,
        "RequestLimitPolicyList": [
            {
                "PolicyId": "ccRule-00009xn0",
                "InstanceId": "bgp-00000001",
                "Ip": "1.1.1.1",
                "Protocol": "http",
                "Domain": "www.test.com",
                "PolicyRecord": {
                    "Period": 10,
                    "RequestNum": 500,
                    "Action": "alg",
                    "ExecuteDuration": 120,
                    "Mode": "equal",
                    "Uri": "/",
                    "UserAgent": "",
                    "Cookie": ""
                },
                "CreateTime": "2022-12-02 09:11:48",
                "ModifyTime": "2022-12-02 09:11:48"
            }
        ]
    }
}
```

