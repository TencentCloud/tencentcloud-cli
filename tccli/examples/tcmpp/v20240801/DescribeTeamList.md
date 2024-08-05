**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTeamList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --Keyword abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "TeamId": "abc",
                    "TeamName": "abc",
                    "AdminUserId": "abc",
                    "AdminUserAccount": "abc",
                    "AdminUserName": "abc",
                    "MemberCount": 0,
                    "TeamRoleTypeList": [
                        0
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

