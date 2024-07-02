**Example 1: 获取扫描报告列表**

获取扫描报告列表

Input: 

```
tccli csip DescribeScanReportList --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": "1300*****",
                "AssetCount": 33,
                "Progress": 100,
                "ReportId": "rpt-**********",
                "ReportName": "标准体检_标准体检_*********",
                "ScanPlan": 0,
                "Status": 2,
                "TaskId": "rmis-*********",
                "TaskName": "标准体检_**********",
                "TaskTime": "2024-07-01 00:19:17",
                "UIN": "100**********",
                "UserName": "天******"
            }
        ],
        "RequestId": "3d9b475f-**********",
        "TotalCount": 22,
        "UINList": [
            "100*****"
        ]
    }
}
```

