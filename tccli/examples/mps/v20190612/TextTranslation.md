**Example 1: 文本翻译请求示例**



Input: 

```
tccli mps TextTranslation --cli-unfold-argument  \
    --SourceText hello \
    --Source zh \
    --Target en
```

Output: 
```
{
    "Response": {
        "RequestId": "6411c585-ee14-4a53-8642-dea0f16e161d",
        "Source": "zh",
        "Target": "en",
        "TargetText": "hello"
    }
}
```

