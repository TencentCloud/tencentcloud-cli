**Example 1: Using policy matching to delete inbound policies of security groups**



Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 37 \
    --SecurityGroupPolicySet.Ingress.0.ServiceTemplate.ServiceGroupId ppmg-ei8hfd9a \
    --SecurityGroupPolicySet.Ingress.0.CidrBlock 10.9.89.9/25 \
    --SecurityGroupPolicySet.Ingress.0.Action accept
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 2: Using policy matching to delete outbound policies of security groups**



Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 38 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceGroupId ppmg-ei8hfd9a \
    --SecurityGroupPolicySet.Egress.0.CidrBlock 10.9.89.9/25 \
    --SecurityGroupPolicySet.Egress.0.Action accept
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 3: Using index matching to delete inbound policies of security groups**



Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 39 \
    --SecurityGroupPolicySet.Ingress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Ingress.1.PolicyIndex 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

**Example 4: Using index matching to delete outbound policies of security groups**



Input: 

```
tccli vpc DeleteSecurityGroupPolicies --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 40 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 0 \
    --SecurityGroupPolicySet.Egress.1.PolicyIndex 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

