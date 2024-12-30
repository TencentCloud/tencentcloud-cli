**Example 1: 创建新账号**



Input: 

```
tccli lighthousedb CreateAccounts --cli-unfold-argument  \
    --ClusterId lhdbmysql-00000000 \
    --Accounts.0.AccountName andyUser \
    --Accounts.0.AccountPassword Pass@3306 \
    --Accounts.0.Description desc \
    --Accounts.0.Host %
```

Output: 
```
{
    "Response": {
        "RequestId": "724e2b99-0ede-4fad-a608-ab7557fa0ede"
    }
}
```

