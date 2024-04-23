**Example 1: 创建新账号**



Input: 

```
tccli lighthousedb CreateAccounts --cli-unfold-argument  \
    --ClusterId lhdbmysql-00000000 \
    --Accounts.0.AccountName test \
    --Accounts.0.AccountPassword password \
    --Accounts.0.Description desc \
    --Accounts.0.Host %
```

Output: 
```
{
    "Response": {
        "RequestId": "176669"
    }
}
```

