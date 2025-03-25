**Example 1: 查询异步任务列表**

查询异步任务列表

Input: 

```
tccli organization ListTasks --cli-unfold-argument  \
    --ZoneId z-djwidnwidj \
    --PrincipalId u-xj8sncidnc \
    --NextToken xownw8db38dbe8fne==- \
    --MaxResults 1 \
    --PrincipalType User \
    --TargetUin 1000023423 \
    --TargetType Member \
    --RoleConfigurationId rc-xjw9dsmw \
    --Status InProgress \
    --TaskType CreateRoleAssignment
```

Output: 
```
{
    "Response": {
        "NextToken": "sgt*****",
        "TotalCounts": 1,
        "MaxResults": 10,
        "IsTruncated": true,
        "Tasks": [
            {
                "TaskId": "t-xsinsxinsdk",
                "RoleConfigurationId": "rc-xmw9xjdsd",
                "RoleConfigurationName": "配置",
                "TargetUin": 1000232234,
                "TargetType": "User",
                "PrincipalId": "u-xm89dnsujs",
                "PrincipalType": "Member",
                "TaskType": "CreateRoleAssignment",
                "Status": "InProgress",
                "FailureReason": ""
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

