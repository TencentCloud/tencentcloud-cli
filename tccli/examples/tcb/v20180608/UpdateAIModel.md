**Example 1: 更新模型列表**

更新模型列表

Input: 

```
tccli tcb UpdateAIModel --cli-unfold-argument  \
    --EnvId httpservice-wushan-8devh79e82d2a \
    --GroupName cloudbase-test \
    --Models.0.Model hy3-preview
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "dffc99bc-c381-4d74-9bf4-ec8e141ea3bd"
    }
}
```

