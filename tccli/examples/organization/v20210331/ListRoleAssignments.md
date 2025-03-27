**Example 1: 查询授权列表**

查询授权列表

Input: 

```
tccli organization ListRoleAssignments --cli-unfold-argument  \
    --ZoneId z-ssmdsowm** \
    --RoleConfigurationId rc2-as245usjsm \
    --MaxResults 30 \
    --NextToken  \
    --TargetType MemeberUin \
    --TargetUin 10000238922 \
    --PrincipalType User \
    --PrincipalId u-ss342md**
```

Output: 
```
{
    "Response": {
        "NextToken": "xgt******",
        "TotalCounts": 30,
        "MaxResults": 10,
        "IsTruncated": true,
        "RoleAssignments": [
            {
                "RoleConfigurationId": "ec-swidn****",
                "RoleConfigurationName": "conf1",
                "TargetUin": 100000322,
                "TargetType": "MemberUin",
                "TargetName": "user1",
                "PrincipalId": "u-ssiisn***",
                "PrincipalType": "User",
                "PrincipalName": "testConfig",
                "CreateTime": "2024-01-01 12:12:12",
                "UpdateTime": "2024-01-01 12:12:12"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

