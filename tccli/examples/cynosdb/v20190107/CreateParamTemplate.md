**Example 1: 创建参数模板**

创建参数模板

Input: 

```
tccli cynosdb CreateParamTemplate --cli-unfold-argument  \
    --TemplateDescription 常用模版 \
    --EngineVersion 5.7 \
    --TemplateId 93 \
    --TemplateName 5.7常用参数模版
```

Output: 
```
{
    "Response": {
        "RequestId": "b7735dc6-5847-4c9b-a713-9745f9afda34",
        "TemplateId": 95
    }
}
```

**Example 2: 自定义参数模板**

自定义参数模板

Input: 

```
tccli cynosdb CreateParamTemplate --cli-unfold-argument  \
    --TemplateDescription API测试 \
    --EngineVersion 5.7 \
    --TemplateId 0 \
    --DbMode NORMAL \
    --TemplateName API测试
```

Output: 
```
{
    "Response": {
        "RequestId": "edbd6b65-daf0-4ca8-b34f-cc3fd42790d8",
        "TemplateId": 27
    }
}
```

