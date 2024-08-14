**Example 1: 删除子用户同步任务**

删除子用户同步任务

Input: 

```
tccli organization DeleteUserSyncProvisioning --cli-unfold-argument  \
    --ZoneId z-dssmowmsd \
    --UserProvisioningId up-sxins8snds
```

Output: 
```
{
    "Response": {
        "Tasks": {
            "TaskId": "t-duedin****",
            "TargetUin": 1000289211,
            "TargetType": "MemberUin",
            "TaskType": "DeleteProvisioning",
            "TaskStatus": "InProgress",
            "UserProvisioningId": "upe-d8n3d9***",
            "PrincipalId": "u-dend83***",
            "PrincipalType": "User",
            "PrincipalName": "test",
            "DuplicationStrategy": "KeepBoth",
            "DeletionStrategy": "Delete"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

