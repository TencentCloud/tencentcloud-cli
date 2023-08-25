**Example 1: 获取资产报表任务列表**

获取资产报表任务列表

Input: 

```
tccli dsgc DescribeReportTasks --cli-unfold-argument  \
    --DspaId abc \
    --ReportName abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ItemSet": [
            {
                "Id": 1,
                "ReportName": "abc",
                "ReportType": "abc",
                "ReportPeriod": 1,
                "ReportPlan": 1,
                "ReportStatus": "abc",
                "TimingStartTime": "abc",
                "CreateTime": "abc",
                "FinishedTime": "abc",
                "SubUin": "abc",
                "FailedMessage": "abc",
                "Enable": 1,
                "ComplianceName": "abc",
                "ProgressPercent": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

