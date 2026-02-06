**Example 1: 删除分析集群账号**



Input: 

```
tccli cynosdb DeleteLibraDBClusterAccounts --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --Accounts.0.AccountName Admin \
    --Accounts.0.Host %
```

Output: 
```
{
    "Response": {
        "RequestId": "b813e2cc-814e-43d3-9cb4-02986ba485b3"
    }
}
```

