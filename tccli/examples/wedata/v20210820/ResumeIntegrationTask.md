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

