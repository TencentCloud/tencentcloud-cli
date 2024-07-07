**Example 1: 开启密码轮转**



Input: 

```
tccli cdb CreateRotationPassword --cli-unfold-argument  \
    --InstanceId abc \
    --Accounts.0.User abc \
    --Accounts.0.Host abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

