**Example 1: 查询**



Input: 

```
tccli cdwdoris DescribeUserPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --UserName abc \
    --PassWord abc \
    --WhiteHost abc
```

Output: 
```
{
    "Response": {
        "AccountInfo": {
            "UserName": "abc",
            "Host": "%",
            "UserDescription": ""
        },
        "Permissions": [
            {
                "GlobalPermissions": null,
                "CatalogPermissions": [
                    {
                        "CatalogName": "internal",
                        "Permissions": [
                            "SELECT_PRIV",
                            "LOAD_PRIV",
                            "ALTER_PRIV",
                            "CREATE_PRIV",
                            "DROP_PRIV"
                        ]
                    }
                ],
                "DatabasePermissions": null,
                "TablePermissions": null
            }
        ],
        "RequestId": "xxx-xx-xx-xx-xxxx"
    }
}
```

