**Example 1: 解绑弹性公网IP ACL**



Input: 

```
tccli bmeip UnbindEipAcls --cli-unfold-argument  \
    --EipIdAclIdList.0.EipId eip-pq9cuew0 \
    --EipIdAclIdList.0.AclId bmeipacl-s1hf4voq
```

Output: 
```
{
    "Response": {
        "RequestId": "05f46f45-5cc1-428d-bc66-3231344e760d"
    }
}
```

