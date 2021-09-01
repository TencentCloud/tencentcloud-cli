**Example 1: Sending regular emails**



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

