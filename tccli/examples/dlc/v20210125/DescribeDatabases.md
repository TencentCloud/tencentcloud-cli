**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli dlc DescribeDatabases --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --KeyWord database1 \
    --DatasourceConnectionName DataLakeCatalog \
    --Sort CreateTime
```

Output: 
```
{
    "Response": {
        "DatabaseList": [
            {
                "Comment": "default description",
                "CreateTime": "1737372787000",
                "DatabaseName": "database1",
                "GovernPolicy": {
                    "RuleType": "none"
                },
                "Location": "",
                "ModifiedTime": "1737372787000",
                "Properties": [
                    {
                        "Key": "param1",
                        "Value": "default param"
                    }
                ],
                "UserAlias": "",
                "UserSubUin": ""
            }
        ],
        "RequestId": "********-****-****-****-2d2f1a350edb",
        "TotalCount": 1
    }
}
```

