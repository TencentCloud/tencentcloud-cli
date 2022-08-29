**Example 1: 查询VM策略**



Input: 

```
tccli vpc DescribeVmPolicyInternal --cli-unfold-argument  \
    --GetVMPolicyRequest.0.Uuid sg-aassaa
```

Output: 
```
{
    "Response": {
        "VMPolicySet": [
            {
                "Uuid": "84f9a2ad-6659-4864-808c-bd17f3c2acea",
                "ErrorCode": 0,
                "Policy": [
                    {
                        "Ip": "111.108.86.20"
                    },
                    {
                        "Ip": "111.108.86.20"
                    }
                ],
                "IsolateLevel": 0
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

