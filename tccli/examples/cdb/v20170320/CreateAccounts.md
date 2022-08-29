**Example 1: 创建云数据库的账户**



Input: 

```
tccli cdb CreateAccounts --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --Password fsdgfdgfd \
    --Accounts.0.Host 127.0.0.1 \
    --Accounts.0.User ajnnw \
    --Description description
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

