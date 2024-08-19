**Example 1: 修改数据库的权限**

以数据库维度修改权限

Input: 

```
tccli sqlserver ModifyDatabasePrivilege --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --DataBaseSet.0.DataBaseName testuser \
    --DataBaseSet.0.AccountPrivileges.0.UserName testdb \
    --DataBaseSet.0.AccountPrivileges.0.Privilege ReadOnly
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab",
        "FlowId": "30321"
    }
}
```

