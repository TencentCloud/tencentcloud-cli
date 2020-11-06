**Example 1: Modifying instance account permissions**



Input: 

```
tccli sqlserver ModifyAccountPrivilege --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Accounts.0.UserName testuser \
    --Accounts.0.DBPrivileges.0.DBName testdb \
    --Accounts.0.DBPrivileges.0.Privilege ReadOnly
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

