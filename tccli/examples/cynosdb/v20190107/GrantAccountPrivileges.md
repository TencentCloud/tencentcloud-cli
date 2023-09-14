**Example 1: 批量授权账号权限**

批量授权账号权限

Input: 

```
tccli cynosdb GrantAccountPrivileges --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --DbTablePrivileges ALTER DROP \
    --Account.AccountName test \
    --Account.Host % \
    --DbTables.0.Db test1 \
    --DbTables.0.TableName user1 \
    --DbTables.1.Db test2
```

Output: 
```
{
    "Response": {
        "RequestId": "147706"
    }
}
```

