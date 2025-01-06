**Example 1: 创建实例公网访问多白名单策略**



Input: 

```
tccli tcr CreateMultipleSecurityPolicy --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --SecurityGroupPolicySet.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.0.Description desc1 \
    --SecurityGroupPolicySet.0.CidrBlock 1.1.1.1 \
    --SecurityGroupPolicySet.0.PolicyVersion 1 \
    --SecurityGroupPolicySet.1.PolicyIndex 1 \
    --SecurityGroupPolicySet.1.Description desc2 \
    --SecurityGroupPolicySet.1.CidrBlock 2.2.2.2 \
    --SecurityGroupPolicySet.1.PolicyVersion 2
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-dg284imq",
        "RequestId": "ecac515a-323e-4517-a1a2-d81c2ceeed99"
    }
}
```

