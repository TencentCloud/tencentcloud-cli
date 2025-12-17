**Example 1: 查询用户权限**



Input: 

```
tccli tccatalog DescribeRolesPrivilegeList --cli-unfold-argument  \
    --UserId 700002198531 \
    --Limit 10 \
    --Offset 0 \
    --OrderBy policy-source \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "SecurableObjects": [
            {
                "FullName": "DataL***talog",
                "Privileges": {
                    "Condition": "allow",
                    "Name": "use_***log"
                },
                "SourceId": 700002198531,
                "SourceName": "_default_***02198531",
                "Type": "catalog"
            }
        ],
        "TotalCount": 15,
        "RequestId": "fb034622-5a23-449e-9202-a8942ad282a9"
    }
}
```

