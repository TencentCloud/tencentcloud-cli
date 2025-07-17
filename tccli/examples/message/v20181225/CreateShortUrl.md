**Example 1: 创建短链**



Input: 

```
tccli message CreateShortUrl --cli-unfold-argument  \
    --Url https://cloud.tencent.com/act/pro/cloudbase-discuzq11 \
    --ValidPeriod 3600 \
    --Creator etherzhou
```

Output: 
```
{
    "Response": {
        "ShortUrl": "https://mc.tencent.com/ZfWTo6Jb",
        "RequestId": "a6642212-e83b-47bc-bf5c-8e22b32bd72f"
    }
}
```

