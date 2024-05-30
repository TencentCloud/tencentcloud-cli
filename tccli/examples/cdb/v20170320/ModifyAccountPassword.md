**Example 1: 修改云数据库实例账号的密码**



Input: 

```
tccli cdb ModifyAccountPassword --cli-unfold-argument  \
    --InstanceId cdb-xxxx \
    --NewPassword your_new_password \
    --Accounts.0.Host % \
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

