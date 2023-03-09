**Example 1: 发送注册邮箱验证码**



Input: 

```
tccli account SendEmailVerifyCode --cli-unfold-argument  \
    --Email test@qq.com \
    --ClientIP 192.168.1.1 \
    --Lang zh
```

Output: 
```
{
    "Response": {
        "RequestId": "049d2419-5c81-45ee-be29-fbaa6f12804a"
    }
}
```

