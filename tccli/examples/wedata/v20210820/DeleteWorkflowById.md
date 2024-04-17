**Example 1: 删除工作流**

删除工作流

Input: 

```
tccli wedata DeleteWorkflowById --cli-unfold-argument  \
    --WorkflowId 1520b2bc-f0f4-11ee-8s13-a4ae120f8272 \
    --ProjectId 1531609692220365952 \
    --DeleteMode True \
    --EnableNotify True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "ResultMsg": null,
            "ErrorId": null,
            "ErrorDesc": null
        },
        "RequestId": "46db9784-4083-44fc-99f3-f942babc1b93"
    }
}
```

