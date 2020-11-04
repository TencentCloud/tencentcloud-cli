**Example 1: 修改安全组出站和入站规则**



Input: 

```
tccli vpc ModifySecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12\
    --SecurityGroupId sg-ohuuioma\
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da\
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6\
    --SecurityGroupPolicySet.Egress.0.Action accept\
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy\
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceId ppm-f5n1f8da\
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressId ipm-2uw6ujo6\
    --SecurityGroupPolicySet.Ingress.0.Action accept\
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription Test
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

