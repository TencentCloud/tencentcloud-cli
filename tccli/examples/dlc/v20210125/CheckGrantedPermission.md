**Example 1: 检查权限状态**



Input: 

```
tccli dlc CheckGrantedPermission --cli-unfold-argument  \
    --CheckPermission.0.AccessType show \
    --CheckPermission.0.ResourceBaseInfo.Catalog DataLakeCatalog \
    --CheckPermission.0.ResourceBaseInfo.Schema schema1 \
    --CheckPermission.0.ResourceBaseInfo.Table table1 \
    --CheckPermission.0.ResourceBaseInfo.View view1 \
    --CheckPermission.0.ResourceBaseInfo.Database database1 \
    --CheckPermission.0.ResourceBaseInfo.Function function1
```

Output: 
```
{
    "Response": {
        "PermissionResponses": [
            {
                "AccessType": "select",
                "ResourceBaseInfo": {
                    "Catalog": "DataLakeCatalog",
                    "Schema": "schema1",
                    "Table": "table1"
                },
                "Allowed": true
            }
        ],
        "RequestId": "********-****-****-****-12345678"
    }
}
```

