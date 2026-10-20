**Example 1: 创建权限申请范围**



Input: 

```
tccli organization CreateRoleConfigurationApplyScope --cli-unfold-argument  \
    --ZoneId z-hmdjcgbvm7z2 \
    --ApplyScopeInfo.0.PrincipalId u-dm5nub3hl6ur \
    --ApplyScopeInfo.0.PrincipalType User \
    --ApplyScopeInfo.0.TargetUin 700002529727 \
    --ApplyScopeInfo.0.TargetType MemberUin \
    --ApplyScopeInfo.0.RoleConfigurationId rc-0lvaff6ddbn4
```

Output: 
```
{
    "Response": {
        "SuccessCount": 2,
        "RequestId": "b08547f2-52ee-4489-afac-833c62b1a8f7"
    }
}
```

