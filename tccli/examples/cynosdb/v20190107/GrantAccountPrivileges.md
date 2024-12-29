**Example 1: 批量授权账号权限**

批量授权账号权限

Input: 

```
tccli cynosdb GrantAccountPrivileges --cli-unfold-argument  \
    --ClusterId cynosdbmysql-j9i41hdd \
    --DbTablePrivileges ALTER DROP \
    --Account.AccountName andy \
    --Account.Host % \
    --DbTables.0.Db db1 \
    --DbTables.0.TableName user1 \
    --DbTables.1.Db db2
```

Output: 
```
{
    "Response": {
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

