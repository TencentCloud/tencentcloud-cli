**Example 1: 批量回收账号权限**



Input: 

```
tccli cynosdb RevokeAccountPrivileges --cli-unfold-argument  \
    --Account.Host % \
    --Account.AccountName test \
    --DbTablePrivileges ALTER \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --DbTables.0.TableName test-table \
    --DbTables.0.Db test-db
```

Output: 
```
{
    "Response": {
        "RequestId": "147706"
    }
}
```

