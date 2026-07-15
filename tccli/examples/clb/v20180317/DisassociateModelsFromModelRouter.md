**Example 1: 模型从模型路由实例解除关联**



Input: 

```
tccli clb DisassociateModelsFromModelRouter --cli-unfold-argument  \
    --ModelRouterId cmr-h2tdbhtz \
    --Models.0.ModelName gpt-4o \
    --Models.0.Provider openai \
    --Models.0.Type BYOK \
    --Models.0.ServiceProviderId model-pb9cvzsua
```

Output: 
```
{
    "Response": {
        "RequestId": "e32f5696-3439-4983-bc25-22a263c14ef0"
    }
}
```

