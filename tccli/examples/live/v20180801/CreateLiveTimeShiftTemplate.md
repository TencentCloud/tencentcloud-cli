**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveTimeShiftTemplate --cli-unfold-argument  \
    --Description xx \
    --TranscodeTemplateIds 0 \
    --RemoveWatermark True \
    --TemplateName xx \
    --ItemDuration 1 \
    --Duration 1 \
    --Area xx
```

Output: 
```
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

