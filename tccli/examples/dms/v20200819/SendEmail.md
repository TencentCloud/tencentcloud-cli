**Example 1: 发送普通邮件**



Input: 

```
tccli dms SendEmail --cli-unfold-argument  \
    --FromAddress test@example.com \
    --ToAddress to@example.com \
    --ReplyAdress reply@example.com \
    --Subject subject
```

Output: 
```
{
    "result": true
}
```

