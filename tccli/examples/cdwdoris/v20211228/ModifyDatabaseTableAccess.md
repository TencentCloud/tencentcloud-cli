**Example 1: 授权**



Input: 

```
tccli cdwdoris ModifyDatabaseTableAccess --cli-unfold-argument  \
    --InstanceId cdwdoris-7da9fumk \
    --Database demo1 \
    --Table my_table \
    --Privileges SELECT_PRIV LOAD_PRIV \
    --GrantOrRevoke GRANT \
    --CatalogName internal
```

Output: 
```
{
    "Response": {
        "Success": true,
        "Message": "Permissions granted successfully.",
        "RequestId": "xxxx-xxxx-xxxx-xxxx"
    }
}
```

