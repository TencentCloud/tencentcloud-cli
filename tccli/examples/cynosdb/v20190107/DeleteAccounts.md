**Example 1: 删除账号**



Input: 

```
tccli cynosdb DeleteAccounts --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ixgbd0di \
    --Accounts.0.AccountName admin \
    --Accounts.0.Host myHost
```

Output: 
```
{
    "Response": {
        "RequestId": "120440"
    }
}
```

