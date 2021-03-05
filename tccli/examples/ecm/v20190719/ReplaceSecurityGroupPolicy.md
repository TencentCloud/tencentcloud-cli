**Example 1: 替换单条安全组路由规则**



Input: 

```
tccli ecm ReplaceSecurityGroupPolicy --cli-unfold-argument  \
    --SecurityGroupId esg-ohuuioma \
    --SecurityGroupPolicySet.Version 20 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.0.Protocol tcp \
    --SecurityGroupPolicySet.Egress.0.Port 8080 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 10.0.0.0/24 \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy
```

Output: 
```
{
    "Response": {}
}
```

