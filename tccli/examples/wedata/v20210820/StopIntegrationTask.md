**Example 1: 停止集成任务**

停止集成任务

Input: 

```
tccli wedata StopIntegrationTask --cli-unfold-argument  \
    --ProjectId xx \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Data": true
    }
}
```

