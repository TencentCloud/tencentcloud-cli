**Example 1: 暂停集成任务**

暂停集成任务

Input: 

```
tccli wedata SuspendIntegrationTask --cli-unfold-argument  \
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

