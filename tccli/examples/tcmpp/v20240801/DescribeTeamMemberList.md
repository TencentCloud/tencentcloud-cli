**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTeamMemberList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --TeamId abc \
    --Keyword abc \
    --RoleIds 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "UserId": "abc",
                    "UserAccount": "abc",
                    "UserName": "abc",
                    "TeamId": "abc",
                    "TeamName": "abc",
                    "TeamRoleName": "abc",
                    "TeamRoleId": 0,
                    "CanEdit": true
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

