**Example 1: 解除权限配置在成员账号上的部署**

解除权限配置在成员账号上的部署

Input: 

```
tccli organization DismantleRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-disanisa \
    --RoleConfigurationId rc-daosmqa \
    --TargetType Member \
    --TargetUin 1000023292
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

