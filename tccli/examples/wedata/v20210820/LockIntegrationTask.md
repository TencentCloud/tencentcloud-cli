**Example 1: 锁定集成任务**

锁定集成任务

Input: 

```
tccli wedata LockIntegrationTask --cli-unfold-argument  \
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

