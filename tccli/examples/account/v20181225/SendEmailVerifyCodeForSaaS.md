**Example 1: 发送成功示例**



Input: 

```
tccli account SendEmailVerifyCodeForSaaS --cli-unfold-argument  \
    --Email ahal@qq.com \
    --UserIP 127.0.0.1 \
    --Lang en \
    --CaptchaAppId  \
    --Ticket  \
    --Random 
```

Output: 
```
{
    "Response": {
        "RequestId": "e87879b8-f0a4-456d-affb-8ebe986a314e"
    }
}
```

