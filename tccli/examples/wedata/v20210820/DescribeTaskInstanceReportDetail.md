**Example 1: 离线任务实例统计明细**



Input: 

```
tccli wedata DescribeTaskInstanceReportDetail --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 202205058668886 \
    --CurRunDate 2020-05-05 12:00:00 \
    --IssueDate 2020-05-05 12:04:18
```

Output: 
```
{
    "Response": {
        "Summary": {
            "TotalReadRecords": 2000000,
            "TotalReadBytes": 89898292,
            "TotalWriteRecords": 2000000,
            "TotalWriteBytes": 89898292,
            "RecordSpeed": 8000,
            "ByteSpeed": 3.5,
            "TotalErrorRecords": 0,
            "TotalErrorBytes": 0,
            "TotalRunDuration": 308,
            "BeginRunTime": "2020-05-05 12:00:00",
            "EndRunTime": "2020-05-05 12:05:08"
        },
        "ReadNode": {
            "NodeName": "mysql_input_node",
            "DataSource": "datasource.table",
            "TotalReadRecords": 2000000,
            "TotalReadBytes": 89898292,
            "RecordSpeed": 8000,
            "ByteSpeed": 3.5,
            "TotalErrorRecords": 0
        },
        "WriteNode": {
            "NodeName": "mysql_input_node",
            "DataSource": "datasource.table",
            "TotalWriteRecords": 2000000,
            "TotalWriteBytes": 89898292,
            "RecordSpeed": 8000,
            "ByteSpeed": 3.5,
            "TotalErrorRecords": 0
        },
        "RequestId": "xx"
    }
}
```

