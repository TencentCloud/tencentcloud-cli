**Example 1: 查询指定用户申请范围列表**



Input: 

```
tccli organization ListRoleConfigurationApplyScopes --cli-unfold-argument  \
    --ZoneId z-hmdjcgbvm7z2 \
    --PrincipalId u-dm5nub3hl6ur \
    --PrincipalType User \
    --TargetUin 700002529727 \
    --Filter  \
    --MaxResults 20 \
    --NextToken 
```

Output: 
```
{
    "Response": {
        "ApplyScopes": [
            {
                "CreateTime": "2026-07-03 15:09:13",
                "PrincipalId": "u-dm5nub3hl6ur",
                "PrincipalName": "1122",
                "PrincipalType": "User",
                "RoleConfigurationId": "rc-0lvaff6ddbn4",
                "RoleConfigurationName": "RoleConfig04",
                "TargetName": "smz23",
                "TargetType": "MemberUin",
                "TargetUin": 700002529727,
                "UpdateTime": "2026-07-03 15:09:13"
            }
        ],
        "IsTruncated": false,
        "MaxResults": 20,
        "NextToken": "",
        "TotalCounts": 1,
        "RequestId": "0510fe32-9815-4db9-ae15-da9c3c43ee01"
    }
}
```

