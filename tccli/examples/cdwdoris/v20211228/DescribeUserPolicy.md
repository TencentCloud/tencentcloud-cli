**Example 1: 获取 Doris 用户的详细信息，包括账户信息、权限主机和权限配置。**



Input: 

```
tccli cdwdoris DescribeUserPolicy --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --UserName user1 \
    --PassWord 1****dz \
    --WhiteHost %
```

Output: 
```
{
    "Response": {
        "AccountInfo": {
            "Host": "%",
            "UserDescription": "",
            "UserName": "user1"
        },
        "Permissions": {
            "CatalogPermissions": null,
            "DatabasePermissions": null,
            "GlobalPermissions": [
                "ADMIN_PRIV"
            ],
            "TablePermissions": null
        },
        "RequestId": "4b63a3b4-2900-4d47-b536-2fd80ccc16dd"
    }
}
```

