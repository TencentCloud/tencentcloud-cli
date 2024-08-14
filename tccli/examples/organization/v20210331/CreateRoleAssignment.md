**Example 1:  在成员账号上授权**

 在成员账号上授权

Input: 

```
tccli organization CreateRoleAssignment --cli-unfold-argument  \
    --ZoneId z-djw83n*** \
    --RoleAssignmentInfo.0.RoleConfigurationId rc-sjsiw2*** \
    --RoleAssignmentInfo.0.TargetType MemberUin \
    --RoleAssignmentInfo.0.TargetUin 1000023222 \
    --RoleAssignmentInfo.0.PrincipalType User \
    --RoleAssignmentInfo.0.PrincipalId u-0829jd8d***
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "TaskId": "t-sowmiwm",
                "RoleConfigurationId": "r-sjsosmsss",
                "RoleConfigurationName": "test",
                "TargetUin": 10000323432,
                "TargetType": "MemberUin",
                "PrincipalId": "u-djiem3o***",
                "PrincipalType": "User",
                "TaskType": "CreateRoleAssignment",
                "Status": "InProgress"
            }
        ],
        "RequestId": "10accfa5-15ed-41fa-9e09-7efffd8e9345"
    }
}
```

