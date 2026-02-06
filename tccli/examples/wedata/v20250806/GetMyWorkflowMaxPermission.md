**Example 1: 成功示例**



Input: 

```
tccli wedata GetMyWorkflowMaxPermission --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --EntityId 2d5f5074-45b7-11f0-8ec8-b8599f277de5 \
    --EntityType folder
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionType": "CAN_MANAGE"
        },
        "RequestId": "d1fa40f6-f497-430e-b499-abf4a7bb30e9"
    }
}
```

