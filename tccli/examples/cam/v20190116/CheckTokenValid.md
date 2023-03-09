**Example 1: 检验saas登录态**



Input: 

```
tccli cam CheckTokenValid --cli-unfold-argument  \
    --SaaSToken 100000009472 \
    --Platform coding \
    --TokenUin 123456 \
    --TokenOwnerUin 123456 \
    --ClientIP 127.0.0.1 \
    --ClientUA chrome
```

Output: 
```
{
    "Response": {
        "RequestId": 0
    }
}
```

