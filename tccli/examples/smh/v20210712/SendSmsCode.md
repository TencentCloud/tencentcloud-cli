**Example 1: 发送短信验证码**



Input: 

```
tccli smh SendSmsCode --cli-unfold-argument  \
    --Purpose BindSuperAdmin \
    --InstanceId n0v9tdme \
    --PhoneNumber 18999999999
```

Output: 
```
{
    "Response": {
        "RequestId": "37c3c855-caee-4c44-9778-bdec5998e5f1"
    }
}
```

