**Example 1: 设置暴力破解阻断开关状态**



Input: 

```
tccli csip ModifyBruteAttackBanStatus --cli-unfold-argument  \
    --OpenSmartMode True \
    --BanBlackIp True \
    --BanVulIp True \
    --BanByRule True
```

Output: 
```
{
    "Response": {
        "RequestId": "ec878600-87bc-4246-9607-xxxxxxxx"
    }
}
```

