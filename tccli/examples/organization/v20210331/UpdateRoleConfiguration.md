**Example 1: 修改权限配置信息**

修改权限配置信息

Input: 

```
tccli organization UpdateRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-6yd36d1vqmy0 \
    --RoleConfigurationId rc-c03cbnjbbzyb \
    --NewDescription this is role configuration \
    --NewSessionDuration 900 \
    --NewRelayState https://console.cloud.tencent.com
```

Output: 
```
{
    "Response": {
        "RoleConfigurationInfo": {
            "CreateTime": "2026-08-25 15:02:46",
            "Description": "this is role configuration",
            "RelayState": "https://console.cloud.tencent.com",
            "RoleConfigurationId": "rc-c03cbnjbbzyb",
            "RoleConfigurationName": "session-duration-rc",
            "SessionDuration": 900,
            "UpdateTime": "2026-08-27 11:26:24"
        },
        "RequestId": "d2e38d16-a94d-4687-8f51-760c28c368be"
    }
}
```

