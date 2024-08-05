**Example 1: demo**

demo

Input: 

```
tccli tcmpp AddTeamMember --cli-unfold-argument  \
    --TeamId abc \
    --MemberList.0.UserId abc \
    --MemberList.0.UserRoleId 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "abc"
    }
}
```

