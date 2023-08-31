**Example 1: 创建安全组**

创建安全组

Input: 

```
tccli vpc CreateSecurityGroupWithPolicies --cli-unfold-argument  \
    --GroupName TestGroup \
    --GroupDescription test-group-desc
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33",
            "UpdateTime": "2018-01-13 19:26:33",
            "TagSet": [],
            "IsDefault": false
        }
    }
}
```

**Example 2: 创建安全组和安全组规则**

创建安全组和安全组规则

Input: 

```
tccli vpc CreateSecurityGroupWithPolicies --cli-unfold-argument  \
    --GroupName TestGroup \
    --GroupDescription test-group-desc \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy \
    --SecurityGroupPolicySet.Egress.1.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.1.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.1.ServiceTemplate.ServiceGroupId ppmg-f5n1f8da \
    --SecurityGroupPolicySet.Egress.1.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.1.AddressTemplate.AddressGroupId ipmg-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.1.Action accept \
    --SecurityGroupPolicySet.Egress.1.PolicyDescription Test
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12345678",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33",
            "UpdateTime": "2018-01-13 19:26:33",
            "TagSet": [],
            "IsDefault": false
        }
    }
}
```

