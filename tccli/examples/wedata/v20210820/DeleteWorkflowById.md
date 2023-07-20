**Example 1: 删除工作流**

删除工作流

Input: 

```
tccli wedata DeleteWorkflowById --cli-unfold-argument  \
    --WorkflowId abc \
    --ProjectId abc \
    --DeleteMode True \
    --EnableNotify True
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

