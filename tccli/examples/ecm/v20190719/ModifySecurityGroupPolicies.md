**Example 1: 修改安全组出站和入站规则**



Input: 

```
tccli ecm ModifySecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId esg-ohuuioma \
    --SecurityGroupPolicySet.Egress.0.Protocol TCP \
    --SecurityGroupPolicySet.Egress.0.Port 80 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 10.0.0.0/16 \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription demo \
    --SecurityGroupPolicySet.Ingress.0.Protocol TCP \
    --SecurityGroupPolicySet.Ingress.0.Port 8080 \
    --SecurityGroupPolicySet.Ingress.0.Action accept \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 10.0.0.0/16 \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription demo
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

