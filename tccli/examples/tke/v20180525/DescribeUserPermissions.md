**Example 1: 查询子账号权限**



Input: 

```
tccli tke DescribeUserPermissions --cli-unfold-argument  \
    --TargetUin 700002308532
```

Output: 
```
{
    "Response": {
        "Permissions": [
            {
                "ClusterId": "cls-n17663rk",
                "IsCustom": false,
                "Namespace": "",
                "RoleName": "tke:admin",
                "RoleType": "cluster"
            }
        ],
        "TargetUin": "700002308532",
        "RequestId": "6c830591-6462-43c6-8740-28c1e03c2b45"
    }
}
```

