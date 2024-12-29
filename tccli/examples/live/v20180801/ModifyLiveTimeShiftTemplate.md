**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveTimeShiftTemplate --cli-unfold-argument  \
    --TemplateId 1 \
    --TemplateName timeshift \
    --Description timeshift \
    --Duration 1 \
    --ItemDuration 1 \
    --RemoveWatermark True \
    --TranscodeTemplateIds 0 \
    --Area 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

