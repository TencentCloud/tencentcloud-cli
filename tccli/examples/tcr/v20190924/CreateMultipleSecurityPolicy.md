**Example 1: 创建实例公网访问多白名单策略**



Input: 

```
tccli tcr CreateMultipleSecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --SecurityGroupPolicySet.0.CidrBlock 192.168.0.0/24 \
    --SecurityGroupPolicySet.0.Description test
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

