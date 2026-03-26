**Example 1: 修改谷歌认证源**

修改谷歌认证源

Input: 

```
tccli tcb ModifyProvider --cli-unfold-argument  \
    --EnvId lowcode-xxx \
    --Id google \
    --Name.Message Google \
    --Name.Localized.0.Locale zh \
    --Name.Localized.0.Message 谷歌 \
    --ProviderType OIDC \
    --Picture https://example.com/google.svg \
    --Homepage https://google.com \
    --Config.Issuer http://accounts.google.com \
    --Config.ResponseType id_token
```

Output: 
```
{
    "Response": {
        "RequestId": "74402479-adf8-47aa-9479-0dd0e922d024"
    }
}
```

**Example 2: 修改邮箱认证源**



Input: 

```
tccli tcb ModifyProvider --cli-unfold-argument  \
    --EnvId tcb-env-01 \
    --Id email \
    --EmailConfig.On FALSE \
    --EmailConfig.SmtpConfig.SenderAddress 123@qq.com \
    --EmailConfig.SmtpConfig.ServerHost smtp.qq.com \
    --EmailConfig.SmtpConfig.ServerPort 465 \
    --EmailConfig.SmtpConfig.AccountUsername 123@qq.com \
    --EmailConfig.SmtpConfig.AccountPassword xyzvyu \
    --EmailConfig.SmtpConfig.SecurityMode SSL
```

Output: 
```
{
    "Response": {
        "RequestId": "74402479-adf8-47aa-9479-0dd0e922d024"
    }
}
```

