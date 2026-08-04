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

**Example 2: 将模型关联到模型路由实例并指定BYOK实例的调度权重**

将模型关联到模型路由实例指定BYOK实例的调度权重

Input: 

```
tccli clb AssociateModelsToModelRouter --cli-unfold-argument  \
    --ModelRouterId cmr-mwmjm160 \
    --Models.0.ModelName my-gpt-5 \
    --Models.0.Provider openai \
    --Models.0.Type BYOK \
    --Models.0.ServiceProviderId byok-r9ue6gow \
    --Models.0.Order 2 \
    --Models.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "9c0c97f3-c26e-4ae7-a228-e92a088cd9d6"
    }
}
```

