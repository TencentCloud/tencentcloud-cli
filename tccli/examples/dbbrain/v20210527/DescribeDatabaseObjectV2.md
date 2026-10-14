**Example 1: 查询建表语句**



Input: 

```
tccli dbbrain DescribeDatabaseObjectV2 --cli-unfold-argument  \
    --Product sqlserver \
    --ObjectType TableStatistics \
    --InstanceId mssql-15rso1sb \
    --TableSchema test_object \
    --TableName sales.t_obj_dup
```

Output: 
```
{
    "Response": {
        "TableName": "t_obj_dup",
        "TableSchema": "test_object",
        "TableStatistics": {
            "DataFree": 0.05,
            "DataLength": 0.02,
            "DatabaseName": "test_object",
            "Engine": "SqlServer",
            "FragRatio": 71.43,
            "IndexLength": 0,
            "PhysicalFileSize": 0.1,
            "TableName": "t_obj_dup",
            "TableRows": 1,
            "TableSchema": "sales",
            "TotalLength": 0.07,
            "UsedLength": 0.02
        },
        "RequestId": "fcaa610b-4a75-4b13-b88f-b4e2672f7322"
    }
}
```

