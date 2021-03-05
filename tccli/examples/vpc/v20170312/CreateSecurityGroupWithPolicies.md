**Example 1: 创建安全组**



Input: 

```
tccli vpc CreateSecurityGroupWithPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --GroupName TestGroup \
    --GroupDescription test-group-desc
```

Output: 
```
{
    "Response": {
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0"
        }
    }
}
```

**Example 2: 创建安全组和安全组规则**



Input: 

```
tccli vpc CreateSecurityGroupWithPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --GroupName TestGroup \
    --GroupDescription test-group-desc \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
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
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0"
        }
    }
}
```

