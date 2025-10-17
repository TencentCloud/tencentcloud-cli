**Example 1: 查询函数类型**



Input: 

```
tccli wedata DescribeFunctionTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ErrorMessage": null,
        "RequestId": "ac62b8e2-679e-4c06-ba2d-be87377f082c",
        "Types": [
            {
                "EnName": "Hive Sql 函数",
                "Name": "HIVE",
                "ZhName": "Hive Sql 函数"
            },
            {
                "EnName": "Spark Sql 函数",
                "Name": "SPARK",
                "ZhName": "Spark Sql 函数"
            },
            {
                "EnName": "DLC Sql 函数",
                "Name": "DLC",
                "ZhName": "DLC Sql 函数"
            },
            {
                "EnName": "CDW PostgreSQL 函数",
                "Name": "CDW_POSTGRESQL",
                "ZhName": "CDW PostgreSQL 函数"
            }
        ]
    }
}
```

