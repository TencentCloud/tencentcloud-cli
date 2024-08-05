**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeRoleDetail --cli-unfold-argument  \
    --RoleId 0 \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "RoleId": 0,
            "RoleName": "abc",
            "TeamId": "abc",
            "TeamName": "abc",
            "ResourceIds": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

