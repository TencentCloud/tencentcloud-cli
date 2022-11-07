**Example 1: 离线任务周期统计明细**



Input: 

```
tccli wedata DescribeTaskReportDetailList --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 202205058668886 \
    --BeginDate 2022-05-01 \
    --EndDate 2022-05-05 \
    --StateList 1,2 \
    --SortItem startDate \
    --SortType DESC \
    --PageIndex 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskId": "202205058668000",
                "InstanceId": "202205058668000",
                "CurRunDate": "2020-05-05 12:00:00",
                "IssueDate": "2020-05-05 12:01:00",
                "TaskState": "2",
                "TotalReadRecords": 2000000,
                "TotalReadBytes": 89898292,
                "TotalWriteRecords": 2000000,
                "TotalWriteBytes": 89898292,
                "RecordSpeed": 8000,
                "ByteSpeed": 3.5,
                "TotalErrorRecords": 0
            }
        ],
        "PageIndex": 1,
        "PageSize": 10,
        "TotalCount": 29,
        "TotalPage": 3,
        "RequestId": "xx"
    }
}
```

