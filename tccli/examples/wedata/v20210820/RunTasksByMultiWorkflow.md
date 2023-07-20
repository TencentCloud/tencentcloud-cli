**Example 1: 批量启动工作流**

批量启动工作流

Input: 

```
tccli wedata RunTasksByMultiWorkflow --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowIds abc \
    --EnableMakeUp 1
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

