**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata GetTriggerWorkflow --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId c6df7416-ee03-405e-adf1-094d26b8c98b
```

Output: 
```
{
    "Response": {
        "Data": {
            "BundleId": null,
            "BundleInfo": null,
            "CreateUserUin": null,
            "GeneralTaskParams": [],
            "OwnerUin": "100028579606",
            "Path": "/默认文件夹/test_wk_3",
            "SchedulerStatus": null,
            "TriggerWorkflowSchedulerConfigurations": null,
            "WorkflowDesc": null,
            "WorkflowName": "test_wk_3",
            "WorkflowParams": []
        },
        "RequestId": "90b5193f-a0a0-4e24-8e8d-cfe452f79243"
    }
}
```

