**Example 1: 修改账号权限**



Input: 

```
tccli cynosdb ModifyAccountPrivileges --cli-unfold-argument  \
    --ClusterId xxx \
    --Account.AccountName xxx \
    --Account.Host xx \
    --GlobalPrivileges xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "147706"
    }
}
```

