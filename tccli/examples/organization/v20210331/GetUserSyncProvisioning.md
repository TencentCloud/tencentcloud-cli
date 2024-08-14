**Example 1: 查询CAM用户同步**

查询CAM用户同步

Input: 

```
tccli organization GetUserSyncProvisioning --cli-unfold-argument  \
    --ZoneId z-dimd3d*** \
    --UserProvisioningId up-imei3rdiem
```

Output: 
```
{
    "Response": {
        "UserProvisioning": {
            "UserProvisioningId": "up-siwnei3nso",
            "Description": "this is cam user sync",
            "Status": "Enabled",
            "PrincipalId": "u-swnd8wn3",
            "PrincipalName": "test",
            "PrincipalType": "User",
            "TargetUin": "10000338332",
            "TargetName": "test",
            "TargetType": "MemberUin",
            "DuplicationStrategy": "KeepBoth",
            "DeletionStrategy": "Delete",
            "CreateTime": "2024-01-01 12:12:12",
            "UpdateTime": "2024-01-01 12:12:12"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

