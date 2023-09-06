**Example 1: 创建用户账号**

创建用户账号

Input: 

```
tccli cynosdb CreateAccounts --cli-unfold-argument  \
    --ClusterId abc \
    --Accounts.0.AccountName test \
    --Accounts.0.AccountPassword 888888@Abcde \
    --Accounts.0.Host 1.1.1.1 \
    --Accounts.0.Description abc \
    --Accounts.0.MaxUserConnections 10
```

Output: 
```
{
    "Response": {
        "RequestId": "176669"
    }
}
```

