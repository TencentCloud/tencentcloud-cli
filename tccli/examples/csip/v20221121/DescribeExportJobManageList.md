**Example 1: 导出任务列表**



Input: 

```
tccli csip DescribeExportJobManageList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ExportJobStatus": "SUCCESS",
                "ExportProgress": 0,
                "FailureMsg": "",
                "InsertTime": "2025-01-14T09:06:25Z",
                "JobID": "cc518a49-273a-4076-80c8-f5f5e5bfea95",
                "JobName": "Exposure-1300056410-250114170625-1",
                "Source": "Exposure",
                "Timeout": "2025-01-14T10:06:25Z"
            }
        ],
        "RequestId": "649979d5-a371-41b5-becf-dd67ce2e0523",
        "TotalCount": 43
    }
}
```

