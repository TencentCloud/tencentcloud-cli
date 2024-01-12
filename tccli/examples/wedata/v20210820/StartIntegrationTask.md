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

**Example 2: mock**

mock

Input: 

```
tccli wedata StartIntegrationTask --cli-unfold-argument  \
    --TaskId abcde \
    --ProjectId 12345
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "f09a4fcb-63b3-44a1-89e4-841f3491faff"
    }
}
```

