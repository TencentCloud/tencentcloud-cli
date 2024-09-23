**Example 1: 修改数据库所有者**



Input: 

```
tccli postgres ModifyDatabaseOwner --cli-unfold-argument  \
    --DBInstanceId postgres-mnhbbw99 \
    --DatabaseName testdatabase \
    --DatabaseOwner test
```

Output: 
```
{
    "Response": {
        "RequestId": "a11906eb-75b4-43c4-8d3e-aa6b2991c8f5"
    }
}
```

