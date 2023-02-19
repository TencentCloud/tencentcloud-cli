**Example 1: 修改安全组出站和入站规则**

修改安全组出站和入站规则

Input: 

```
tccli vpc ModifySecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Ingress.0.Action accept \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription Test \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

