**Example 1: 批量回收账号权限**

批量回收账号权限

Input: 

```
tccli cynosdb RevokeAccountPrivileges --cli-unfold-argument  \
    --Account.Host % \
    --Account.AccountName andy \
    --DbTablePrivileges ALTER \
    --ClusterId cynosdbmysql-j9i41hkf \
    --DbTables.0.TableName andy-table \
    --DbTables.0.Db andy-db
```

Output: 
```
{
    "Response": {
        "RequestId": "347698da-03e4-4078-8d96-9a8b219c01a5"
    }
}
```

