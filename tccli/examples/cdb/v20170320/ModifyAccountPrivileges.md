**Example 1: 修改账号权限**

修改账号权限时授予全局WITH GRANT OPTION权限

Input: 

```
tccli cdb ModifyAccountPrivileges --cli-unfold-argument  \
    --InstanceId cdb-iun70ygb \
    --Accounts.0.User user \
    --Accounts.0.Host % \
    --GlobalPrivileges SELECT \
    --DatabasePrivileges.0.Privileges SELECT \
    --DatabasePrivileges.0.Database Custom \
    --TablePrivileges.0.Database Custom \
    --TablePrivileges.0.Table Product \
    --TablePrivileges.0.Privileges SELECT \
    --ColumnPrivileges.0.Database Custom \
    --ColumnPrivileges.0.Table Product \
    --ColumnPrivileges.0.Column category \
    --ColumnPrivileges.0.Privileges SELECT
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "d1ad7033-496c905f-6af10457-3b283706",
        "RequestId": "23626d57-74d4-483d-8a8e-a81162050fe5"
    }
}
```

