**Example 1: 获取扫描报告列表**

获取扫描报告列表

Input: 

```
tccli csip DescribeScanReportList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "TaskId": "xx",
                "TaskName": "xx",
                "Status": 0,
                "Progress": 0,
                "TaskTime": "xx",
                "ReportId": "xx",
                "ReportName": "xx",
                "ScanPlan": 0,
                "AssetCount": 0,
                "AppId": "xx",
                "UIN": "xx",
                "UserName": "xx"
            }
        ],
        "UINList": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

