**Example 1: 弹性网关关联安全组**

将指定网卡和指定安全组进行关联

Input: 

```
tccli vpc AssociateNetworkInterfaceSecurityGroups --cli-unfold-argument  \
    --NetworkInterfaceIds eni-1a2b3c4d \
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

