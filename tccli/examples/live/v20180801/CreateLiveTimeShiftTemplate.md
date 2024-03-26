**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveTimeShiftTemplate --cli-unfold-argument  \
    --TemplateName abc \
    --Description abc \
    --Area abc \
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
        "RequestId": "abc"
    }
}
```

