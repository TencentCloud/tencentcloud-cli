**Example 1: 创建用户账号**

创建用户账号

Input: 

```
tccli cynosdb CreateAccounts --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd45qwe \
    --Accounts.0.AccountName tom \
    --Accounts.0.AccountPassword 888888@Abcde \
    --Accounts.0.Host 1.1.1.1 \
    --Accounts.0.Description AccountDescription \
    --Accounts.0.MaxUserConnections 10
```

Output: 
```
{
    "Response": {
        "RequestId": "2f355036-ad6b-4b09-8d9b-793235f856c5"
    }
}
```

