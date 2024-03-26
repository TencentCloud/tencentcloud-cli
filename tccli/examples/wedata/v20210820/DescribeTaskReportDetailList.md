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
        "PageIndex": 1,
        "PageSize": 1,
        "TotalCount": 1,
        "TotalPage": 1,
        "Items": [
            {
                "TaskId": "abc",
                "InstanceId": "abc",
                "CurRunDate": "abc",
                "IssueDate": "abc",
                "TaskState": "abc",
                "TotalReadRecords": 1,
                "TotalReadBytes": 1,
                "TotalWriteRecords": 1,
                "TotalWriteBytes": 1,
                "RecordSpeed": 1,
                "ByteSpeed": 0,
                "TotalErrorRecords": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

