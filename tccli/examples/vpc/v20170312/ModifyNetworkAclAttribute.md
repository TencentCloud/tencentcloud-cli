**Example 1: Changing the name of a network ACL**



Input: 

```
tccli vpc ModifyNetworkAclAttribute --cli-unfold-argument  \
    --Version 2017-03-12\
    --NetworkAclId acl-12345678\
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

