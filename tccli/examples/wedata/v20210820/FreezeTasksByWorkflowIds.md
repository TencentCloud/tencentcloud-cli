**Example 1: 暂停工作流下的所有任务**

暂停工作流下的所有任务

Input: 

```
tccli wedata FreezeTasksByWorkflowIds --cli-unfold-argument  \
    --WorkflowIds abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ResultMsg": "abc",
            "ErrorId": "abc",
            "ErrorDesc": "abc"
        },
        "RequestId": "abc"
    }
}
```

