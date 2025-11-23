**Example 1: sample**



Input: 

```
tccli waf ModifyBotIdRule --cli-unfold-argument  \
    --Domain admin.com \
    --SceneId 3088902138 \
    --Data.0.RuleId 3309123111 \
    --Data.0.BotId abot \
    --Data.0.Status True \
    --Data.0.Action monitor \
    --GlobalSwitch 0 \
    --Status True \
    --RuleAction redirect \
    --GlobalRedirect /luffy \
    --ProtectLevel normal
```

Output: 
```
{
    "Response": {
        "RequestId": "a713f4cf-51ef-437f-8467-d4fdec061b78"
    }
}
```

