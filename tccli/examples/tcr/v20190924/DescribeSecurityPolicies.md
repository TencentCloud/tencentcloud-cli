**Example 1: 查看实例安全策略**



Input: 

```
tccli tcr DescribeSecurityPolicies --cli-unfold-argument  \
    --RegistryId tcr-test123
```

Output: 
```
{
    "Response": {
        "SecurityPolicySet": [
            {
                "PolicyIndex": 0,
                "CidrBlock": "127.0.0.1/24",
                "Description": "test",
                "PolicyVersion": "1"
            }
        ],
        "RequestId": "xx"
    }
}
```

