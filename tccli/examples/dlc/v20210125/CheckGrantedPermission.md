**Example 1: 检查权限状态**



Input: 

```
tccli dlc CheckGrantedPermission --cli-unfold-argument  \
    --CheckPermission.0.AccessType abc \
    --CheckPermission.0.ResourceBaseInfo.Catalog abc \
    --CheckPermission.0.ResourceBaseInfo.Schema abc \
    --CheckPermission.0.ResourceBaseInfo.Table abc \
    --CheckPermission.0.ResourceBaseInfo.View abc
```

Output: 
```
{
    "Response": {
        "PermissionResponses": [
            {
                "AccessType": "abc",
                "ResourceBaseInfo": {
                    "Catalog": "abc",
                    "Schema": "abc",
                    "Table": "abc",
                    "View": "abc",
                    "Database": "abc",
                    "Function": "abc"
                },
                "Allowed": true
            }
        ],
        "RequestId": "abc"
    }
}
```

