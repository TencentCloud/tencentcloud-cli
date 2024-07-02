**Example 1: 获取任务扫描报告列表**

获取任务扫描报告列表

Input: 

```
tccli csip DescribeTaskLogList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": "130*****",
                "AssetsNumber": 33,
                "ReportType": 1,
                "RiskNumber": 45,
                "StartTime": "2024-07-01 00:00:15",
                "Status": 2,
                "TaskCenterTaskId": "rmis-************",
                "TaskLogId": "rpt-*********",
                "TaskLogName": "标准体检_*********",
                "TaskName": "标准体检_***********",
                "TemplateId": 2,
                "Time": "2024-07-01 00:19:17",
                "UIN": "1000******",
                "UserName": "天******"
            }
        ],
        "NotViewNumber": 42,
        "ReportTemplateNumber": 1,
        "RequestId": "04355839-***********",
        "TotalCount": 51
    }
}
```

