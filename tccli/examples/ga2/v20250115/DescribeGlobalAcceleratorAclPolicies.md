**Example 1: 查看访问控制策略**



Input: 

```
tccli ga2 DescribeGlobalAcceleratorAclPolicies --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka
```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorAclPolicySet": [
            {
                "DefaultAction": "ACCEPT",
                "GlobalAcceleratorAclPolicyId": "sp-00000msz",
                "Status": "OPEN"
            }
        ],
        "RequestId": "72b61d0e-a0c8-4db9-b069-6a85b80cea9d",
        "TotalCount": 1
    }
}
```

