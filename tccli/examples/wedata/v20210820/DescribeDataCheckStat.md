**Example 1: 数据检测情况**



Input: 

```
tccli wedata DescribeDataCheckStat --cli-unfold-argument  \
    --ProjectId 153160990365952 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "TableTotal": 1,
            "ColumnTotal": 1,
            "TableConfig": 1,
            "ColumnConfig": 1,
            "TableExec": 1,
            "ColumnExec": 1
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

