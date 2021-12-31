**Example 1: 获取角色权限边界**



Input: 

```
tccli cam GetRolePermissionBoundary --cli-unfold-argument  \
    --RoleId 1234567
```

Output: 
```
{
    "Response": {
        "PolicyId": 123456,
        "PolicyType": 1,
        "CreateMode": 5,
        "PolicyName": "QcloudCOSAccessForCLSRole,QcloudCKAFKAAccessForCLSRole",
        "PolicyDocument": "{\"strategyInfo\":{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":\"*\",\"resource\":\"*\"}]}}",
        "RequestId": "c3da1c1c-df35-467d-9335-99c68d993e0a"
    }
}
```

