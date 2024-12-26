**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveTimeShiftTemplate --cli-unfold-argument  \
    --TemplateName name \
    --Description timeshift \
    --Area 0 \
    --Duration 1 \
    --ItemDuration 1 \
    --RemoveWatermark True \
    --TranscodeTemplateIds 0
```

Output: 
```
{
    "Response": {
        "TemplateId": 0,
        "RequestId": "3fefec28-3f95-4055-8a22-714cc271251e"
    }
}
```

