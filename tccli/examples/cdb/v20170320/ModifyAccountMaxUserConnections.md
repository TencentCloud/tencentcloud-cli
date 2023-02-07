**Example 1: 修改云数据库账户最大可用连接数**



Input: 

```
tccli cdb ModifyAccountMaxUserConnections --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --MaxUserConnections 100 \
    --Accounts.0.Host 127.0.0.1 \
    --Accounts.0.User ajnnw
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

