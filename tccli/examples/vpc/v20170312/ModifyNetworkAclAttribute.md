**Example 1: 修改网络ACL名称**



Input: 

```
tccli vpc ModifyNetworkAclAttribute --cli-unfold-argument  \
    --NetworkAclId acl-12345678 \
    --NetworkAclName 'test modify'
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

