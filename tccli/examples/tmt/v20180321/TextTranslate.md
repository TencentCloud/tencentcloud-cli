**Example 1: 文本翻译调用示例**

文本翻译

Input: 

```
tccli tmt TextTranslate --cli-unfold-argument  \
    --SourceText hello \
    --Source en \
    --Target zh \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "TargetText": "你好",
        "Source": "en",
        "Target": "zh",
        "RequestId": "000ee211-f19e-4a34-a214-e2bb1122d248"
    }
}
```

