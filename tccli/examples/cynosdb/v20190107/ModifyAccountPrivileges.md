**Example 1: 修改账号库表权限**

修改账号库表权限

Input: 

```
tccli cynosdb ModifyAccountPrivileges --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxx \
    --Account.AccountName andy \
    --Account.Host 1.1.1.1 \
    --GlobalPrivileges CREATE \
    --DatabasePrivileges.0.Db testDb \
    --DatabasePrivileges.0.Privileges DELETE \
    --TablePrivileges.0.Db testDb \
    --TablePrivileges.0.TableName testTable \
    --TablePrivileges.0.Privileges DROP
```

Output: 
```
{
    "Response": {
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

