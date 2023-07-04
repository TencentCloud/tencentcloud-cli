**Example 1: 提交集成任务**

提交集成任务

Input: 

```
tccli wedata CommitIntegrationTask --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc \
    --CommitType 0 \
    --TaskType 1 \
    --ExtConfig.0.Name abc \
    --ExtConfig.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "1x",
        "Data": true
    }
}
```

