**Example 1: 批量启动工作流**

批量启动工作流

Input: 

```
tccli wedata RunTasksByMultiWorkflow --cli-unfold-argument  \
    --ProjectId 1531609696090322952 \
    --WorkflowIds 1520b2bc-f0f4-11ee-8d13-a4ae120f8272 \
    --EnableMakeUp 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ResultMsg": "",
            "ErrorId": "",
            "ErrorDesc": ""
        },
        "RequestId": "0b2bc-f0f4-11ee-8d13-a4ae12072"
    }
}
```

