**Example 1: API调用**



Input: 

```
tccli tmt TextTranslate --cli-unfold-argument  \
    --SourceText hello \
    --ProjectId 0 \
    --Target zh \
    --Source en
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

