**Example 1: 启动集成任务**

启动集成任务

Input: 

```
tccli wedata StartIntegrationTask --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc \
    --Event abc \
    --ExtConfig.0.Name abc \
    --ExtConfig.0.Value abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

