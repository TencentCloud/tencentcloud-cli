**Example 1: 成功**

成功

Input: 

```
tccli wedata CheckTaskPriorityDs --cli-unfold-argument  \
    --ProjectId abc \
    --Tasks.0.TaskId abc \
    --Tasks.0.WorkflowId abc
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

