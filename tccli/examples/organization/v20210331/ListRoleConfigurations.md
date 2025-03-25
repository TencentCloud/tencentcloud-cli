**Example 1: 查询权限配置列表**

查询权限配置列表

Input: 

```
tccli organization ListRoleConfigurations --cli-unfold-argument  \
    --ZoneId z-s9h39sdn2 \
    --NextToken sisndpmfisdnlk \
    --MaxResults 10 \
    --Filter conf1
```

Output: 
```
{
    "Response": {
        "TotalCounts": 20,
        "MaxResults": 10,
        "IsTruncated": true,
        "NextToken": "3si2ns92ns82bos",
        "RoleConfigurations": [
            {
                "RoleConfigurationId": "rc-s2ns92ns***",
                "RoleConfigurationName": "conf1",
                "Description": "this is role configuration",
                "SessionDuration": 900,
                "RelayState": "https://console.cloud.tencent.com",
                "CreateTime": "2019-01-01 12:12:12",
                "UpdateTime": "2019-01-01 12:12:12"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

