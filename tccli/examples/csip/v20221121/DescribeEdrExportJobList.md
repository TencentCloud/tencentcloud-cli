**Example 1: 查看edr导出列表**



Input: 

```
tccli csip DescribeEdrExportJobList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ExportProgress": 100,
                "ExportStatus": "SUCCESS",
                "FailureMsg": "",
                "InsertTime": "2026-05-13 14:31:14",
                "JobId": "3a419bbc-780b-4e8d-882a-9493b4473608",
                "JobName": "EdrAlert_20260513143114_1",
                "Source": "EdrAlert",
                "Timeout": "2026-05-13 16:31:14"
            }
        ],
        "TotalCount": 1,
        "RequestId": "bd0cb02d-add9-4382-b38d-93c75ec7d31f"
    }
}
```

