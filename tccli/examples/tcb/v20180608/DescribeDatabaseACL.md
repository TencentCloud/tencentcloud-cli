**Example 1: 查询数据库ACL**

查询数据库集合的ACL

Input: 

```
tccli tcb DescribeDatabaseACL --cli-unfold-argument  \
    --EnvId env-xxyyzzaa \
    --CollectionName table-abc
```

Output: 
```
{
    "Response": {
        "AclTag": "READONLY",
        "RequestId": "uuid-here"
    }
}
```

