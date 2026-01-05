**Example 1: 修改任务责任人示例**



Input: 

```
tccli wedata UpdateOpsTriggerTasksOwner --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --OwnerIds 100028448903 \
    --TaskIds 20251111191225392
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncActionId": "7628d964-52bc-4eb2-9ab2-db3f0894bbab",
            "FailedCount": 0,
            "SuccessCount": 1,
            "TotalCount": 1
        },
        "RequestId": "c83c7eb1-1ec9-4c33-878f-f46534996f1a"
    }
}
```

