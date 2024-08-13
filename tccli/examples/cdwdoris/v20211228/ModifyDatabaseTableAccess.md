**Example 1: 授权**



Input: 

```
tccli cdwdoris ModifyDatabaseTableAccess --cli-unfold-argument  \
    --Database abc \
    --Table abc \
    --Privileges abc \
    --Role abc \
    --GrantOrRevoke abc \
    --UserName abc \
    --PassWord abc
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

