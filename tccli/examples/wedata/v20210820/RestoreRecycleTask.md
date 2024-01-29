**Example 1: 还原任务**

还原任务

Input: 

```
tccli wedata RestoreRecycleTask --cli-unfold-argument  \
    --TaskId abc \
    --WorkflowId abc \
    --ProjectId abc \
    --TaskName abc \
    --ProductName abc \
    --VirtualFlag True \
    --VirtualTaskId abc \
    --FileRemotePath abc
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

