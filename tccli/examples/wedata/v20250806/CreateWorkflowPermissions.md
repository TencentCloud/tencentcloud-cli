**Example 1: 成功示例**



Input: 

```
tccli wedata CreateWorkflowPermissions --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --EntityId d5f5074-45b7-11f0-8ec8-b8599f277de5 \
    --EntityType folder \
    --PermissionList.0.PermissionTargetType user \
    --PermissionList.0.PermissionTargetId 100028578851 \
    --PermissionList.0.PermissionTypeList CAN_MANAGE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "e38f1ceb-5f58-4d57-acd8-a24e447f1aae"
    }
}
```

