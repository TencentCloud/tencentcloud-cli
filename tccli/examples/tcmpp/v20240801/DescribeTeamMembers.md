**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTeamMembers --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --TeamId abc \
    --PlatformId abc
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
                    "UserRoles": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

