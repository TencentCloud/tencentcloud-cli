**Example 1: 添加网站防护服务器**



Input: 

```
tccli cwp CreateProtectServer --cli-unfold-argument  \
    --ProtectDir /tmp \
    --ProtectHostConfig.0.Quuid quuid \
    --ProtectHostConfig.0.ProtectSwitch 1 \
    --ProtectHostConfig.0.AutoRecovery 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6c251fae-8254-42d8-bd2c-17f54dac1275"
    }
}
```

