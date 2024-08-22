**Example 1: DescribeRoleList**



Input: 

```
tccli tcmpp DescribeRoleList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Keyword  \
    --TeamId 3686677859 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 6,
            "DataList": [
                {
                    "RoleId": 20068,
                    "RoleName": "Application Administrator",
                    "TeamName": "",
                    "CreateTime": "1717575381",
                    "RoleType": 1
                },
                {
                    "RoleId": 20069,
                    "RoleName": "Application Member Manager",
                    "TeamName": "",
                    "CreateTime": "1717575444",
                    "RoleType": 1
                },
                {
                    "RoleId": 20070,
                    "RoleName": "Application Senior Developer",
                    "TeamName": "",
                    "CreateTime": "1717582563",
                    "RoleType": 1
                },
                {
                    "RoleId": 20071,
                    "RoleName": "Application Developer",
                    "TeamName": "",
                    "CreateTime": "1717582775",
                    "RoleType": 1
                },
                {
                    "RoleId": 20072,
                    "RoleName": "Application Operator",
                    "TeamName": "",
                    "CreateTime": "1717582954",
                    "RoleType": 1
                },
                {
                    "RoleId": 20073,
                    "RoleName": "Review Staff",
                    "TeamName": "",
                    "CreateTime": "1717583046",
                    "RoleType": 1
                }
            ]
        },
        "RequestId": "862a6267-d548-4bab-8c39-fad8fdbb33ee"
    }
}
```

