**Example 1: 获取资产报表任务列表**

获取资产报表任务列表

Input: 

```
tccli dsgc DescribeReportTasks --cli-unfold-argument  \
    --DspaId dspa-ab12fd34 \
    --ReportName 资产梳理报告_20241020190049_7aasc462 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ItemSet": [
            {
                "Id": 1,
                "ReportName": "资产梳理报告_20241020190049_7aasc462",
                "ReportType": "database_type",
                "ReportPeriod": 0,
                "ReportPlan": 0,
                "ReportStatus": "Success",
                "TimingStartTime": "2024-10-18 19:00:49",
                "CreateTime": "2024-10-20 19:00:49",
                "FinishedTime": "2024-10-20 19:02:08",
                "SubUin": "700000126513",
                "FailedMessage": "Failed",
                "Enable": 1,
                "ComplianceName": "通用规则集",
                "ProgressPercent": 100,
                "ReportTemplateName": "数据资产分布报告"
            }
        ],
        "RequestId": "9f266ea1-30b1-4941-b513-417660be5e64"
    }
}
```

