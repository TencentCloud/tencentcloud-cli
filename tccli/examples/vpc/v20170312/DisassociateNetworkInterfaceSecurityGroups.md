**Example 1: 弹性网卡解绑安全组**

弹性网卡解绑安全组

Input: 

```
tccli vpc DisassociateNetworkInterfaceSecurityGroups --cli-unfold-argument  \
    --NetworkInterfaceIds eni-12345678 \
    --SecurityGroupIds sg-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

