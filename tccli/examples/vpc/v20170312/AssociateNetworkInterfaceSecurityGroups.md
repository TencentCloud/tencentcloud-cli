**Example 1: Associates an ENI with security groups**



Input: 

```
tccli vpc AssociateNetworkInterfaceSecurityGroups --cli-unfold-argument  \
    --NetworkInterfaceIds eni-1a2b3c4d\
    --SecurityGroupIds sg-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

