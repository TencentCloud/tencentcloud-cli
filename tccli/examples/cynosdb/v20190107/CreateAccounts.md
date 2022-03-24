**Example 1: 创建新账号**



Input: 

```
tccli cynosdb CreateAccounts --cli-unfold-argument  \
    --ClusterId xxx \
    --Accounts.0.AccountName xx \
    --Accounts.0.AccountPassword xxx \
    --Accounts.0.Description xxx \
    --Accounts.0.Host xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "176669"
    }
}
```

