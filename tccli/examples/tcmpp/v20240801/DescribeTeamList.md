**Example 1: DescribeTeamList**



Input: 

```
tccli tcmpp DescribeTeamList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --Keyword  \
    --PlatformId T04827BQ9761718REMX
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "DataList": [
                {
                    "TeamId": "5441555296",
                    "TeamName": "vinya_app",
                    "AdminUserId": "U20240709160550YHSGDN",
                    "AdminUserAccount": "xini_app",
                    "AdminUserName": "xini_app",
                    "MemberCount": 3,
                    "RegisterLink": "/team-register/e2cd77b46a0090bd0e677dca73bda1f3",
                    "TeamRoleTypeList": [
                        2
                    ],
                    "RelatedTeamId": 0
                }
            ]
        },
        "RequestId": "656gg8cd-1651-4c8f-b384-b308ad11f743"
    }
}
```

