**Example 1: 验证短信验证码**



Input: 

```
tccli smh VerifySmsCode --cli-unfold-argument  \
    --Purpose BindSuperAdmin \
    --InstanceId n0v9tdme \
    --PhoneNumber 18999999999 \
    --Code 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "98a878b5-8c16-4788-a7e7-4b1a19a461db"
    }
}
```

