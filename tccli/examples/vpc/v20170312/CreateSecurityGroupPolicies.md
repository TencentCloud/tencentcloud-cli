**Example 1: 安全组添加出站规则**



Input: 

```
tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 21 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy \
    --SecurityGroupPolicySet.Egress.1.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.1.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.1.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.1.Action accept \
    --SecurityGroupPolicySet.Egress.1.PolicyDescription Test
```

Output: 
```
{
    "Response": {
        "RequestID": "53ee3ed3-c9ed-48ba-8a57-8624b9c0d3b8"
    }
}
```

**Example 2: 安全组添加入站规则**



Input: 

```
tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 21 \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.0.Action accept \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription TestPolicy \
    --SecurityGroupPolicySet.Ingress.1.PolicyIndex 1 \
    --SecurityGroupPolicySet.Ingress.1.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.1.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.1.Action accept \
    --SecurityGroupPolicySet.Ingress.1.PolicyDescription Test
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

