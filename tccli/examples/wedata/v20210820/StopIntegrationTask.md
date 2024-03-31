**Example 1: 停止集成任务**

停止集成任务

Input: 

```
tccli wedata StopIntegrationTask --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc
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

