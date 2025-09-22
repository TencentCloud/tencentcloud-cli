**Example 1: GetOpsWorkflow调用实例**



Input: 

```
tccli wedata GetOpsWorkflow --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId 29542955-4f93-44dc-9a16-a6a8231f42cd
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2025-08-22 11:19:24",
            "CycleType": "DAY_CYCLE",
            "EndTime": "2099-12-31 23:59:59",
            "FirstSubmitTime": "2025-08-25 14:52:38",
            "FolderId": "6445aa5a-7e58-11f0-9366-7c8c09fca71c",
            "InstanceInitStrategy": "T_PLUS_0",
            "LatestSubmitTime": "2025-08-25 15:23:15",
            "OwnerUin": ";100042680225;",
            "SchedulerDesc": "每天00:00执行一次",
            "StartTime": "2025-08-25 20:55:34",
            "StartupTime": 0,
            "Status": "ALL_RUNNING",
            "WorkflowDesc": "",
            "WorkflowId": "29542955-4f93-44dc-9a16-a6a8231f42cd",
            "WorkflowName": "fg55",
            "WorkflowType": null
        },
        "RequestId": "f54ed1fa-c6aa-463d-8113-fd94d8d76cd3"
    }
}
```

