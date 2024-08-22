**Example 1: DescribeTeam**



Input: 

```
tccli tcmpp DescribeTeam --cli-unfold-argument  \
    --TeamId 1363731006 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TeamName": "autotest_mini_team",
            "TeamRoleType": 1,
            "AdminUserAccount": "autotest_op",
            "CreateUser": "admin",
            "CreateTime": "1720678574",
            "MemberCount": 8,
            "BindMiniTeamCount": 0,
            "BindTeamName": "autotest_app_team",
            "RegisterLink": "",
            "ApplicationName": "autotest_app"
        },
        "RequestId": "70f3c710-c3ea-46a2-a80d-49100a8acaf7"
    }
}
```

