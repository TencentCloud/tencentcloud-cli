**Example 1: 批量停止工作流**

批量停止工作流

Input: 

```
tccli wedata BatchStopWorkflowsByIds --cli-unfold-argument  \
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

