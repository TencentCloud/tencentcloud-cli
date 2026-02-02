**Example 1: 创建账号**



Input: 

```
tccli cynosdb CreateLibraDBClusterAccounts --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --Accounts.0.AccountName Admin \
    --Accounts.0.AccountPassword Admin*111 \
    --Accounts.0.Host %
```

Output: 
```
{
    "Response": {
        "RequestId": "f7d312b6-48bb-4c10-84f5-4774072355fe"
    }
}
```

