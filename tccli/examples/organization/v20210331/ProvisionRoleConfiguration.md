**Example 1: 将权限配置部署到成员账号上**

将权限配置部署到成员账号上

Input: 

```
tccli organization ProvisionRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-disndw**** \
    --RoleConfigurationId rc-sians9wn**** \
    --TargetType MemberUin \
    --TargetUin 10000293120
```

Output: 
```
{
    "Response": {
        "RequestId": "d95c7cc0-195d-4818-aa3a-e7dc73eafe37",
        "Task": {
            "RoleConfigurationId": "rc-4plmus8fdfsb",
            "RoleConfigurationName": "testConfiguration1",
            "TargetType": "MemberUin",
            "TargetUin": 700000145543,
            "TaskId": "t-2xdmzwphpsbd",
            "TaskStatus": "InProgress",
            "TaskType": "CreateRoleAssignment"
        }
    }
}
```

