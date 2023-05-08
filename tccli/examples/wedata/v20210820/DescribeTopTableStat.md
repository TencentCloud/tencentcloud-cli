**Example 1: 数据表排行**



Input: 

```
tccli wedata DescribeTopTableStat --cli-unfold-argument  \
    --ProjectId 1 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "PipelineTables": [
                {
                    "TableName": "xx",
                    "Cnt": 1,
                    "TableId": "xx"
                }
            ],
            "AlarmTables": [
                {
                    "TableName": "xx",
                    "Cnt": 1,
                    "TableId": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

