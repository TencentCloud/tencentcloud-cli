**Example 1: 绑定弹性公网IP ACL**



Input: 

```
tccli bmeip BindEipAcls --cli-unfold-argument  \
    --EipIdAclIdList.0.EipId eip-pq9cuew0 \
    --EipIdAclIdList.0.AclId bmeipacl-s1hf4voq
```

Output: 
```
{
    "Response": {
        "RequestId": "1e7d04b6-3154-44c1-b3de-e3dfd7767d55"
    }
}
```

