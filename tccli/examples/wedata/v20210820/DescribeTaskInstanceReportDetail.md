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
            "TotalReadRecords": 1,
            "TotalReadBytes": 1,
            "TotalWriteRecords": 1,
            "TotalWriteBytes": 1,
            "RecordSpeed": 1,
            "ByteSpeed": 0,
            "TotalErrorRecords": 1,
            "TotalErrorBytes": 1,
            "TotalRunDuration": 1,
            "BeginRunTime": "2020-05-05 12:00:00",
            "EndRunTime": "2021-05-05 12:00:00"
        },
        "ReadNode": {
            "NodeName": "NodeName",
            "DataSource": "DataSource",
            "TotalReadRecords": 1,
            "TotalReadBytes": 1,
            "RecordSpeed": 1,
            "ByteSpeed": 0,
            "TotalErrorRecords": 1,
            "WaitWriterTime": 0
        },
        "WriteNode": {
            "NodeName": "NodeName",
            "DataSource": "DataSource",
            "TotalWriteRecords": 1,
            "TotalWriteBytes": 1,
            "RecordSpeed": 1,
            "ByteSpeed": 0,
            "TotalErrorRecords": 1,
            "WaitReaderTime": 0
        },
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

