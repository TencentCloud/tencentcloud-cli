**Example 1: 批量停止工作流**

批量停止工作流

Input: 

```
tccli wedata BatchStopWorkflowsByIds --cli-unfold-argument  \
    --WorkflowIds 1520b2bc-f0f4-11ee-2d13-a4ae120f8272 \
    --ProjectId 1531609696090362952
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
        "RequestId": "46db9784-4083-44fc-99f3-f942babc1b93"
    }
}
```

