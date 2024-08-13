**Example 1: 修改权限配置信息**

修改权限配置信息

Input: 

```
tccli organization UpdateRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-22m23mo2 \
    --RoleConfigurationId rc-ai3n9si2m \
    --NewDescription this is role configuration \
    --NewSessionDuration 900 \
    --NewRelayState https://console.cloud.tencent.com
```

Output: 
```
{
    "Response": {
        "RoleConfigurationInfo": {
            "RoleConfigurationId": "rc-s2ns92ns***",
            "RoleConfigurationName": "test",
            "Description": "this is role configuration",
            "SessionDuration": 900,
            "RelayState": "https://console.cloud.tencent.com",
            "CreateTime": "2019-01-01 12:12:12",
            "UpdateTime": "2019-01-01 12:12:12"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

