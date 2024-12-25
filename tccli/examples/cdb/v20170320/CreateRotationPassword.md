**Example 1: 开启密码轮转**



Input: 

```
tccli cdb CreateRotationPassword --cli-unfold-argument  \
    --InstanceId cdb-0zgqlqmd \
    --Accounts.0.User andy \
    --Accounts.0.Host 192.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

