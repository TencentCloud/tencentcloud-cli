**Example 1: 关联支持文本输入的模型**

关联支持文本输入的模型

Input: 

```
tccli clb RegisterModelsToServiceProvider --cli-unfold-argument  \
    --ServiceProviderId byok-7avt6gkt \
    --Models.0.ModelId claude-4-opus \
    --Models.0.ModelAlias claude-4-opus-test-connection \
    --Models.0.InputModalities text
```

Output: 
```
{
    "Response": {
        "RequestId": "689b521b-ab7a-406b-b23d-3317ac07d09e"
    }
}
```

**Example 2: 默认关联模型的请求**



Input: 

```
tccli clb RegisterModelsToServiceProvider --cli-unfold-argument  \
    --ServiceProviderId byok-pegue82p \
    --Models.0.ModelId panda-model-1 \
    --Models.0.ModelAlias panda-model-1
```

Output: 
```
{
    "Response": {
        "RequestId": "9a02d8e9-fb9f-4273-95e1-e3c7722b65b4"
    }
}
```

