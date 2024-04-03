**Example 1: 使用索引匹配删除安全组入站规则**

使用索引匹配删除安全组入站规则

Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-xxxxxxxx \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Ingress.1.PolicyIndex 0 \
    --SecurityGroupPolicySet.Version 39
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 2: 使用索引匹配删除安全组出站规则**

使用索引匹配删除安全组出站规则

Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-xxxxxxxx \
    --SecurityGroupPolicySet.Version 40 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 1 \
    --SecurityGroupPolicySet.Egress.1.PolicyIndex 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 3: 使用规则匹配删除安全组入站规则**

使用规则匹配删除安全组入站规则

Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-xxxxxxxx \
    --SecurityGroupPolicySet.Ingress.0.Action Accept \
    --SecurityGroupPolicySet.Ingress.0.Protocol icmp \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 1.1.1.1/32 \
    --SecurityGroupPolicySet.Ingress.0.Port all \
    --SecurityGroupPolicySet.Version 37
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 4: 使用规则匹配删除安全组出站规则**

使用规则匹配删除安全组出站规则

Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --SecurityGroupId sg-xxxxxxxx \
    --SecurityGroupPolicySet.Version 38 \
    --SecurityGroupPolicySet.Egress.0.Action Accept \
    --SecurityGroupPolicySet.Egress.0.Protocol icmp \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 1.1.1.1/32 \
    --SecurityGroupPolicySet.Egress.0.Port all
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

