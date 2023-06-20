**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli dlc DescribeDatabases --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DatabaseList": [
            {
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
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

