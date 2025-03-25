**Example 1: 查询权限配置信息**

查询权限配置信息

Input: 

```
tccli organization GetRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-2s2osm2*** \
    --RoleConfigurationId rc-odmo23w
```

Output: 
```
{
    "Response": {
        "RoleConfigurationInfo": {
            "RoleConfigurationId": "rc-s2ns92ns***",
            "RoleConfigurationName": "conf1",
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

