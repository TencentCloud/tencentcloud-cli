**Example 1: 修改智能字幕模板**



Input: 

```
tccli mps ModifySmartSubtitleTemplate --cli-unfold-argument  \
    --Definition 202281 \
    --TranslateSwitch ON \
    --Name 新名字 \
    --SubtitleType 1 \
    --TranslateDstLanguage en
```

Output: 
```
{
    "Response": {
        "RequestId": "569d5d19-d01c-4efc-97dc-4ea53ae95647"
    }
}
```

