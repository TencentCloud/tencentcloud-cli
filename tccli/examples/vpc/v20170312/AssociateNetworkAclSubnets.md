**Example 1: 网络ACL关联子网**

网络ACL关联子网

Input: 

```
tccli vpc AssociateNetworkAclSubnets --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --SubnetIds subnet-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

