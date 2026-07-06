**Example 1: 获取日志离线导出任务列表**

获取日志离线导出任务列表

Input: 

```
tccli cfw DescribeOfflineExportTask --cli-unfold-argument  \
    --TaskName test-export \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "322372",
                "TaskName": "flow_border_out_31",
                "DataLength": 0,
                "Progress": 0,
                "Status": 0,
                "ExpireTime": "",
                "ErrorInfo": "",
                "CreateTime": "2025-01-07 09:18:56",
                "UseUserCos": 0
            }
        ],
        "ExportLimit": -1,
        "ExportQuota": 1099511627776,
        "ExportRemainQuota": 1099511627776,
        "RequestId": "64eb2796-219e-4f5c-a2a7-928c2dd99880",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 142440
    }
}
```

