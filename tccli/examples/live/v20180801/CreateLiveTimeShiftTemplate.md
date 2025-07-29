**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveTimeShiftTemplate --cli-unfold-argument  \
    --TemplateName name \
    --Description timeshift \
    --Area 0 \
    --Duration 604800 \
    --ItemDuration 5 \
    --RemoveWatermark False \
    --TranscodeTemplateIds 1
```

Output: 
```
{
    "Response": {
        "TemplateId": 58241,
        "RequestId": "3fefec28-3f95-4055-8a22-714cc271251e"
    }
}
```

