**Example 1: 通过SaaS的登录Code获取token**



Input: 

```
tccli cam GetTokenByAuthCodeForSaaS --cli-unfold-argument  \
    --AuthCode 234564 \
    --Platform meeting \
    --ClientIP 0.0.0.0 \
    --ClientUA chrome
```

Output: 
```
{
    "Response": {
        "Uin": 302000000001,
        "OwnerUin": 302000000001,
        "Token": "35f0******`924",
        "ExpiredTime": 1602995914,
        "RequestId": "12390bee-9701-4179-aefc-7f38a8824e89"
    }
}
```

