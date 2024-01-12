**Example 1: 继续集成任务**

继续集成任务

Input: 

```
tccli wedata ResumeIntegrationTask --cli-unfold-argument  \
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
tccli wedata ResumeIntegrationTask --cli-unfold-argument  \
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
        "RequestId": "5891312f-e0d9-40ef-925c-fdde1cd525af"
    }
}
```

