**Example 1: 创建黑石弹性公网 EIP ACL**

创建黑石弹性公网 EIP ACL

Input: 

```
tccli bmeip CreateEipAcl --cli-unfold-argument  \
    --AclName acltest \
    --Status 0
```

Output: 
```
{
    "Response": {
        "AclId": "bmeipacl-s1hf4voq",
        "Status": 0,
        "AclName": "acltest",
        "CreatedAt": "2018-10-26 14:42:09",
        "RequestId": "471aa00a-04c7-43e2-afb0-33ddb2702ca2"
    }
}
```

