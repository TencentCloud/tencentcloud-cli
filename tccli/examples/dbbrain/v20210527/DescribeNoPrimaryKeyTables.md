**Example 1: 查询实例无主键表**

查询实例无主键表

Input: 

```
tccli dbbrain DescribeNoPrimaryKeyTables --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --Date 2022-04-12
```

Output: 
```
{
    "Response": {
        "RequestId": "8108c1c0-bbcc-11ec-adb9-eb9c1358e03a",
        "NoPrimaryKeyTables": [
            {
                "TableSchema": "demo_schema",
                "TableName": "demo_table",
                "Engine": "InnoDB",
                "TotalLength": 0,
                "TableRows": 0
            }
        ],
        "NoPrimaryKeyTableRecordCount": 8,
        "NoPrimaryKeyTableCount": 8,
        "NoPrimaryKeyTableCountDiff": 0,
        "Timestamp": 1649872593
    }
}
```

