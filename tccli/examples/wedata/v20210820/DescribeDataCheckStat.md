**Example 1: 数据检测情况**



Input: 

```
tccli wedata DescribeDataCheckStat --cli-unfold-argument  \
    --ProjectId 1 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "ColumnConfig": 1,
            "TableExec": 1,
            "ColumnExec": 1,
            "ColumnTotal": 1,
            "TableConfig": 1,
            "TableTotal": 1
        },
        "RequestId": "xx"
    }
}
```

