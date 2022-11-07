**Example 1: 锁定集成任务**

锁定集成任务

Input: 

```
tccli wedata UnlockIntegrationTask --cli-unfold-argument  \
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

