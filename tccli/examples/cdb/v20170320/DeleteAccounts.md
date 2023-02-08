**Example 1: 删除云数据库的账号**



Input: 

```
tccli cdb DeleteAccounts --cli-unfold-argument  \
    --InstanceId xx \
    --Accounts.0.Host 192.168.1.1 \
    --Accounts.0.User user1
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

