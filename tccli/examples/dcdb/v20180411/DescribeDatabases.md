**Example 1: 查询云数据库实例上的数据库列表**



Input: 

```
tccli dcdb DescribeDatabases --cli-unfold-argument  \
    --InstanceId dcdbt-52s53yyh
```

Output: 
```
{
    "Response": {
        "RequestId": "d0f51893-e15f-44ac-be6d-900450a6b8c2",
        "InstanceId": "dcdbt-52s53yyh",
        "Databases": [
            {
                "DbName": "information_schema"
            },
            {
                "DbName": "mysql"
            },
            {
                "DbName": "performance_schema"
            },
            {
                "DbName": "test"
            }
        ]
    }
}
```

