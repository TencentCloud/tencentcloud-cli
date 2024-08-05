**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeRoleList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --Keyword abc \
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
                    "RoleId": 0,
                    "RoleName": "abc",
                    "TeamName": "abc",
                    "CreateTime": "abc",
                    "RoleType": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

