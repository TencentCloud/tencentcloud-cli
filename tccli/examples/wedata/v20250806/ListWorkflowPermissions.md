**Example 1: 成功示例**



Input: 

```
tccli wedata ListWorkflowPermissions --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --EntityId 2d5f5074-45b7-11f0-8ec8-b8599f277de5 \
    --EntityType folder
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "PermissionTargetId": "308335260274237440",
                    "PermissionTargetType": "role",
                    "PermissionTypeList": [
                        "CAN_MANAGE"
                    ]
                },
                {
                    "PermissionTargetId": "100028579801",
                    "PermissionTargetType": "user",
                    "PermissionTypeList": [
                        "CAN_MANAGE"
                    ]
                },
                {
                    "PermissionTargetId": "100028578753",
                    "PermissionTargetType": "user",
                    "PermissionTypeList": [
                        "CAN_MANAGE"
                    ]
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 3,
            "TotalPageNumber": 0
        },
        "RequestId": "477af9ef-2390-47f5-83a8-8546f0130a27"
    }
}
```

