**Example 1: 安全组添加出站规则**

安全组添加出站规则

Input: 

```
tccli vpc CreateSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Ingress.0.Protocol All \
    --SecurityGroupPolicySet.Ingress.0.PolicyDescription 测试 \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressGroupId ipmg-o8w64jdg \
    --SecurityGroupPolicySet.Ingress.0.AddressTemplate.AddressId ipm-ngk4c2dw \
    --SecurityGroupPolicySet.Ingress.0.Ipv6CidrBlock ::/0 \
    --SecurityGroupPolicySet.Ingress.0.SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Ingress.0.ModifyTime 2020-12-03 16:12:15 \
    --SecurityGroupPolicySet.Ingress.0.Action accept \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 0.0.0.0/0 \
    --SecurityGroupPolicySet.Ingress.0.Port 80 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Egress.0.Protocol All \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription 测试 \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressGroupId ipmg-o8w64jdg \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-ngk4c2dw \
    --SecurityGroupPolicySet.Egress.0.Ipv6CidrBlock ::/0 \
    --SecurityGroupPolicySet.Egress.0.SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Egress.0.ModifyTime 2020-12-03 16:12:15 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 0.0.0.0/0 \
    --SecurityGroupPolicySet.Egress.0.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "53ee3ed3-c9ed-48ba-8a57-8624b9c0d3b8"
    }
}
```

