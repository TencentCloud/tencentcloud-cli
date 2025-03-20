**Example 1: 查询导出任务管理列表**



Input: 

```
tccli tcss DescribeExportJobManageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ExportProgress": 0,
                "ExportStatus": "RUNNING",
                "FailureMsg": "FailureMsg",
                "InsertTime": "2024-10-30 10:47:57",
                "JobID": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
                "JobName": "LocalImage-253332865-343433341-1",
                "Source": "LocalImage",
                "Timeout": "2024-10-30 10:47:57"
            }
        ],
        "RequestId": "b0990d92-0eff-4bc3-8484-ffd61d8daa89",
        "TotalCount": 11
    }
}
```

