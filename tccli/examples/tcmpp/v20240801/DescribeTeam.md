**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTeam --cli-unfold-argument  \
    --TeamId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TeamName": "abc",
            "TeamRoleType": 0,
            "AdminUserAccount": "abc",
            "CreateUser": "abc",
            "CreateTime": "abc",
            "MemberCount": 0,
            "BindTeamName": "abc",
            "RegisterLink": "abc"
        },
        "RequestId": "abc"
    }
}
```

