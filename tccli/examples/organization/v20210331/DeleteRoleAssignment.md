**Example 1: 移除成员账号上的授权**

移除成员账号上的授权

Input: 

```
tccli organization DeleteRoleAssignment --cli-unfold-argument  \
    --ZoneId z-2ms923mw \
    --RoleConfigurationId rc-smw9em32 \
    --TargetType MemberUin \
    --TargetUin 10000332 \
    --PrincipalType User \
    --PrincipalId u-siwnwiene \
    --DeprovisionStrategy DeprovisionForLastRoleAssignmentOnAccount
```

Output: 
```
{
    "Response": {
        "Task": {
            "TaskId": "t-0md93jfd3",
            "RoleConfigurationId": "rc-dsk3323",
            "RoleConfigurationName": "conf1",
            "TargetUin": 100032333,
            "TargetType": "MemberUin",
            "PrincipalId": "u-siwnwiene",
            "PrincipalType": "User",
            "TaskType": "DeleteRolesAssignment",
            "Status": "InProgress"
        },
        "RequestId": "abgt*******"
    }
}
```

