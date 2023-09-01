**Example 1: 替换单条安全组路由规则**

替换单条安全组路由规则

Input: 

```
tccli vpc ReplaceSecurityGroupPolicy --cli-unfold-argument  \
    --SecurityGroupId abc \
    --SecurityGroupPolicySet.Version abc \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Egress.0.Protocol UDP \
    --SecurityGroupPolicySet.Egress.0.Port 20 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 61.144.138.34 \
    --SecurityGroupPolicySet.Egress.0.Ipv6CidrBlock ::/0 \
    --SecurityGroupPolicySet.Egress.0.SecurityGroupId sg-1wgfnrnd \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription abc \
    --SecurityGroupPolicySet.Egress.0.ModifyTime 2022-06-21 10:46:42 \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Ingress.0.Protocol UDP \
    --SecurityGroupPolicySet.Ingress.0.Port 20 \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 61.144.138.34 \
    --SecurityGroupPolicySet.Ingress.0.Ipv6CidrBlock ::/0 \
    --SecurityGroupPolicySet.Ingress.0.SecurityGroupId sg-1wgfnrnd \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Ingress.0.Action accept \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription abc \
    --SecurityGroupPolicySet.Ingress.0.ModifyTime 2022-06-21 10:46:42 \
    --OriginalSecurityGroupPolicySet.Version abc \
    --OriginalSecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
    --OriginalSecurityGroupPolicySet.Egress.0.Protocol UDP \
    --OriginalSecurityGroupPolicySet.Egress.0.Port 20 \
    --OriginalSecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --OriginalSecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --OriginalSecurityGroupPolicySet.Egress.0.CidrBlock 61.144.138.34 \
    --OriginalSecurityGroupPolicySet.Egress.0.Ipv6CidrBlock ::/0 \
    --OriginalSecurityGroupPolicySet.Egress.0.SecurityGroupId sg-1wgfnrnd \
    --OriginalSecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --OriginalSecurityGroupPolicySet.Egress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --OriginalSecurityGroupPolicySet.Egress.0.Action accept \
    --OriginalSecurityGroupPolicySet.Egress.0.PolicyDescription abc \
    --OriginalSecurityGroupPolicySet.Egress.0.ModifyTime 2022-06-21 10:46:42
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

