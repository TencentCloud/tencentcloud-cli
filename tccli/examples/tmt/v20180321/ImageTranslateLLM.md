**Example 1: 图片翻译调用示例**



Input: 

```
tccli tmt ImageTranslateLLM --cli-unfold-argument  \
    --Data iVBORw0KGgoAAAAN......Ws0ewAAAABJRU5ErkJggg== \
    --Target en
```

Output: 
```
{
    "Response": {
        "Data": "iVBORw0KGgoAAAANSUh......4AAAAASUVORK5CYII=",
        "RequestId": "962cc025-f31c-466a-9a2d-c7947bd866c2",
        "Source": "zh_CN",
        "SourceText": "你好",
        "Target": "en",
        "TargetText": "Hello"
    }
}
```

