**Example 1: API调用**



Input: 

```
tccli tmt TextTranslate --cli-unfold-argument  \
    --ProjectId 0 \
    --Source en \
    --SourceText hello \
    --Target zh
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

