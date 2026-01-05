**Example 1: 成功示例**



Input: 

```
tccli wedata DeleteWorkflowPermissions --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --EntityId edee3f7f-2f9d-11ef-8ec8-b8599f277de5 \
    --EntityType folder \
    --DeletePermissionList.0.PermissionTargetType user \
    --DeletePermissionList.0.PermissionTargetId 100028578753 \
    --DeletePermissionList.0.PermissionTypeList CAN_MANAGE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "c4fbd90f-6e52-47ef-a240-133eb038d7e8"
    }
}
```

