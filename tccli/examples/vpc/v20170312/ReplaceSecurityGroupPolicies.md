**Example 1: 批量修改安全组规则**

批量修改安全组规则

Input: 

```
tccli vpc ReplaceSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-12345678 \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 3 \
    --SecurityGroupPolicySet.Ingress.0.Protocol tcp \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription TestPolicy \
    --SecurityGroupPolicySet.Ingress.0.Action ACCEPT \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 20.0.0.0/16 \
    --SecurityGroupPolicySet.Ingress.0.Port 22 \
    --SecurityGroupPolicySet.Ingress.1.PolicyIndex 4 \
    --SecurityGroupPolicySet.Ingress.1.Protocol tcp \
    --SecurityGroupPolicySet.Ingress.1.PolicyDescription TestPolicy2 \
    --SecurityGroupPolicySet.Ingress.1.Action DROP \
    --SecurityGroupPolicySet.Ingress.1.CidrBlock 30.0.0.0/16 \
    --SecurityGroupPolicySet.Ingress.1.Port 22 \
    --SecurityGroupPolicySet.Version 20
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

