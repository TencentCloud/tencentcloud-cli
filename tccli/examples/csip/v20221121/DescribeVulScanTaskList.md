**Example 1: 获取漏洞扫描任务记录**



Input: 

```
tccli csip DescribeVulScanTaskList --cli-unfold-argument  \
    --Filters.0.Name JobId \
    --Filters.0.Values 198b38dc1f613b885036e0f78d141c83 \
    --Limit 2 \
    --Offset 0 \
    --Order DESC  \
    --By ScanTime
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Account": 3,
                "AppId": 260083796,
                "Emergency": 1,
                "EndTime": "2026-06-11T16:54:00Z",
                "Id": 134,
                "JobId": "198b38dc1f613b885036e0f78d141c83",
                "KbName": [],
                "Level": [
                    "LOW"
                ],
                "Method": [
                    "VersionCompare"
                ],
                "StartTime": "2026-06-11T15:51:02Z",
                "Status": "SUCCESS",
                "TaskType": 0,
                "VulCategory": [
                    "WEB_CMS"
                ],
                "VulName": []
            }
        ],
        "Total": 1,
        "RequestId": "9f4d3cfa-9941-4f5d-8115-b6f641c8275b"
    }
}
```

