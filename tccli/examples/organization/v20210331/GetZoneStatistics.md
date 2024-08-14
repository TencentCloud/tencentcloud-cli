**Example 1: 查询空间的统计信息**

查询空间的统计信息

Input: 

```
tccli organization GetZoneStatistics --cli-unfold-argument  \
    --ZoneId z-siwns82n****
```

Output: 
```
{
    "Response": {
        "ZoneStatistics": {
            "UserQuota": 1000,
            "GroupQuota": 500,
            "RoleConfigurationQuota": 1000,
            "SystemPolicyPerRoleConfigurationQuota": 20,
            "UserCount": 10,
            "GroupCount": 2,
            "RoleConfigurationCount": 3,
            "UserProvisioningCount": 0,
            "RoleConfigurationSyncCount": 0
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

