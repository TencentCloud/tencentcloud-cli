**Example 1: 查询数据库详细信息**



Input: 

```
tccli dlc DescribeDatabase --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --DatabaseName testDb
```

Output: 
```
{
    "Response": {
        "DatabaseInfo": {
            "DatabaseName": "abc",
            "Comment": "abc",
            "Properties": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "CreateTime": "abc",
            "ModifiedTime": "abc",
            "Location": "abc",
            "UserAlias": "abc",
            "UserSubUin": "abc",
            "GovernPolicy": {
                "RuleType": "abc",
                "GovernEngine": "abc"
            },
            "DatabaseId": "abc"
        },
        "RequestId": "abc"
    }
}
```

