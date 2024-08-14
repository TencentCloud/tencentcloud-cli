**Example 1: 创建子用户同步任务**

创建子用户同步任务

Input: 

```
tccli organization CreateUserSyncProvisioning --cli-unfold-argument  \
    --ZoneId z-di3nd8e*** \
    --UserSyncProvisionings.0.DuplicationStrategy KeepBoth \
    --UserSyncProvisionings.0.DeletionStrategy Delete \
    --UserSyncProvisionings.0.Description this is cam user sync provisioning \
    --UserSyncProvisionings.0.PrincipalId u-sienmcien \
    --UserSyncProvisionings.0.PrincipalType User \
    --UserSyncProvisionings.0.TargetType MemberUin \
    --UserSyncProvisionings.0.TargetUin 1000234382342
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": "t-duedin****",
                "TargetUin": 1000289211,
                "TargetType": "MemberUin",
                "TaskType": "StartProvisioning",
                "TaskStatus": "InProgress",
                "UserProvisioningId": "upe-d8n3d9***",
                "PrincipalId": "u-dend83***",
                "PrincipalType": "User",
                "PrincipalName": "test",
                "DuplicationStrategy": "KeepBoth",
                "DeletionStrategy": "Delete"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-34545s45"
    }
}
```

