**Example 1: 查询修复任务列表**



Input: 

```
tccli csip DescribeVulFixTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 1,
                "TaskId": 10001,
                "VulIds": [
                    10001
                ],
                "KBIds": [],
                "AssetCount": 5,
                "SuccessCount": 3,
                "FailCount": 1,
                "Progress": 80,
                "TargetAppIdsCount": 2,
                "FixStatus": 1,
                "Timeout": 600,
                "StartTime": "2025-06-26T10:00:00+08:00",
                "EndTime": "2025-06-26T10:10:00+08:00",
                "CreateTime": "2025-06-26T09:58:00+08:00",
                "VulNames": [
                    "CVE-2024-12345"
                ],
                "VulCategory": [
                    "LINUX"
                ],
                "AppId": 1251001234
            }
        ],
        "TotalCount": 1,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

