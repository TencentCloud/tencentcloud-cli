**Example 1: 获取租户信息**



Input: 

```
tccli wedata GetWorkspaceTenant --cli-unfold-argument  \
    --WorkspaceId 1769**10*****2*90
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "1***0***87",
            "OwnerUin": "60**00*6***8",
            "VersionInfo": {
                "CreateTime": "2025-11-04 12:26:33",
                "Creator": "6000**56***8",
                "ExpireTime": "2025-11-04 12:26:33",
                "TrialVersionRemainingCu": 0,
                "UpdateTime": "2025-11-04 12:26:33",
                "VersionStatus": 3,
                "VersionType": 2
            }
        },
        "RequestId": "9d5a4661-cb09-4807-9d35-d044956a62fd"
    }
}
```

