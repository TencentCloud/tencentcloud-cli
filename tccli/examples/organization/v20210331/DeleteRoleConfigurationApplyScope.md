**Example 1: 删除权限配置范围**



Input: 

```
tccli organization DeleteRoleConfigurationApplyScope --cli-unfold-argument  \
    --ZoneId z-hmdjcgbvm7z2 \
    --RoleConfigurationIds rc-0lvaff6ddbn4 \
    --TargetUin 700002529727 \
    --PrincipalId u-dm5nub3hl6ur \
    --PrincipalType User
```

Output: 
```
{
    "Response": {
        "RequestId": "d4625a9e-0620-4b16-b906-d00b132e62e0"
    }
}
```

