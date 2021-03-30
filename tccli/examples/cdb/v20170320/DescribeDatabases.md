**Example 1: 查询数据库**



Input: 

```
tccli cdb DescribeDatabases --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "DatabaseList": [
            {
                "CharacterSet": "UTF8",
                "DatabaseName": "test"
            }
        ],
        "TotalCount": 7,
        "Items": [
            "information_schema",
            "mysql",
            "performance_schema",
            "test",
            "trsf1",
            "trsf2",
            "trsf3"
        ]
    }
}
```

