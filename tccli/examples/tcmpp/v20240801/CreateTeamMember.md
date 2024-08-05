**Example 1: demo**

demo

Input: 

```
tccli tcmpp CreateTeamMember --cli-unfold-argument  \
    --UserName abc \
    --UserAccount abc \
    --UserPassword abc \
    --TeamId abc \
    --RoleId 0 \
    --KeyId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "UserId": "abc"
        },
        "RequestId": "abc"
    }
}
```

