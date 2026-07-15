**Example 1: 将模型关联到模型路由实例**



Input: 

```
tccli clb AssociateModelsToModelRouter --cli-unfold-argument  \
    --ModelRouterId cmr-oei1qdkf \
    --Models.0.ModelName gpt-4o \
    --Models.0.Provider openai \
    --Models.0.Type BYOK \
    --Models.0.ServiceProviderId model-pb9cvzsua
```

Output: 
```
{
    "Response": {
        "RequestId": "26c44214-aeb1-46d7-8314-78f54a6e4486"
    }
}
```

