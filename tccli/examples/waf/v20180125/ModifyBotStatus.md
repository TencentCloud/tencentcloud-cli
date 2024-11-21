**Example 1: Bot_V2 bot开关更新**



Input: 

```
tccli waf ModifyBotStatus --cli-unfold-argument  \
    --Category bot \
    --Status 1 \
    --Domain test.com \
    --InstanceID waf_xxx
```

Output: 
```
{
    "Response": {
        "Data": "success",
        "RequestId": "a0b4e55b-5307-4378-856d-efc22475c77d"
    }
}
```

**Example 2: 新版本_bot总开关**



Input: 

```
tccli waf ModifyBotStatus --cli-unfold-argument  \
    --Status 1 \
    --Category bot \
    --Domain fgsta.qcloudwaf.com \
    --IsVersionFour true \
    --BotVersion 4.1.0
```

Output: 
```
{
    "Response": {
        "Data": "success",
        "RequestId": "110a2ef2-74ee-4db1-9b96-7da77283653f"
    }
}
```

**Example 3: 老版本_bot总开关**



Input: 

```
tccli waf ModifyBotStatus --cli-unfold-argument  \
    --Status 0 \
    --Category bot \
    --Domain fgsta.qcloudwaf.com \
    --IsVersionFour true
```

Output: 
```
{
    "Response": {
        "Data": "success",
        "RequestId": "c6ae93c9-f71c-473c-ad9b-ba1b59e47059"
    }
}
```

