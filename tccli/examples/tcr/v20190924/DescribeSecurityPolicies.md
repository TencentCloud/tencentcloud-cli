**Example 1: 查看实例安全策略**



Input: 

```
tccli tcr DescribeSecurityPolicies --cli-unfold-argument  \
    --RegistryId tcr-dg284imq
```

Output: 
```
{
    "Response": {
        "RequestId": "23ff77a4-f5fc-4e2b-b0fa-c85c70676e6a",
        "SecurityPolicySet": [
            {
                "CidrBlock": "47.94.91.32/32",
                "Description": "",
                "PolicyIndex": 0,
                "PolicyVersion": "2"
            },
            {
                "CidrBlock": "0.0.0.0/0",
                "Description": "",
                "PolicyIndex": 1,
                "PolicyVersion": "2"
            }
        ]
    }
}
```

