**Example 1: 安全组添加出站规则**



Input: 

```
tccli ecm CreateSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId esg-ohuuioma \
    --SecurityGroupPolicySet.Version 1 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.0.Protocol TCP \
    --SecurityGroupPolicySet.Egress.0.Port 80 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 10.0.0.0/16 \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy
```

Output: 
```
{
    "Response": {
        "RequestId": "53ee3ed3-c9ed-48ba-8a57-8624b9c0d3b8"
    }
}
```

