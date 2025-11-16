**Example 1: 查看参数模板展开后的安全组规则**

查看参数模板展开后的安全组规则。

Input: 

```
tccli vpc DescribeSecurityGroupExpandedPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-brf5xqjr
```

Output: 
```
{
    "Response": {
        "SecurityGroupPolicySet": {
            "Egress": [],
            "Ingress": [],
            "PolicyStatistics": {
                "EgressIPv4TotalCount": 0,
                "EgressIPv6TotalCount": 0,
                "IngressIPv4TotalCount": 0,
                "IngressIPv6TotalCount": 0
            },
            "Version": "0"
        },
        "RequestId": "492355a4-e313-4f33-8f9a-b5f6a1556e45"
    }
}
```

