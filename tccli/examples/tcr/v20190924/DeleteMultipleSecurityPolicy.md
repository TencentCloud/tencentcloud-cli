**Example 1: 删除实例公网访问白名单策略**



Input: 

```
tccli tcr DeleteMultipleSecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-test123 \
    --SecurityGroupPolicySet.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.0.PolicyVersion 1 \
    --SecurityGroupPolicySet.0.CidrBlock 127.0.0.1/24
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-test123",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

