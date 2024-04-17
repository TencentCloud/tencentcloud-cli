**Example 1: 数据表排行**



Input: 

```
tccli wedata DescribeTopTableStat --cli-unfold-argument  \
    --ProjectId 153160990365952 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmTables": [
                {
                    "TableId": "asfert6345690uijn",
                    "TableName": "test",
                    "Cnt": 1
                }
            ],
            "PipelineTables": [
                {
                    "TableId": "7896tyguhbi79tygui",
                    "TableName": "test",
                    "Cnt": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

