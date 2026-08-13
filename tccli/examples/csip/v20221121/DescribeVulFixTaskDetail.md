**Example 1: 查询修复任务详情**



Input: 

```
tccli csip DescribeVulFixTaskDetail --cli-unfold-argument  \
    --TaskId 10001 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 100001,
                "TaskId": 10001,
                "VulId": 20001,
                "KBId": 0,
                "InstanceId": "ins-a1b2c3d4",
                "MachineName": "web-server-01",
                "MachineIp": "10.0.0.100",
                "VulName": "CVE-2024-12345",
                "Status": 2,
                "FixStatus": 1,
                "SnapshotStatus": 2,
                "SnapshotCreateTime": "2025-06-26T02:00:00Z",
                "SnapshotExpireTime": "2025-07-26T02:00:00Z",
                "ExceptionMessage": "",
                "StartTime": "2025-06-26T10:00:00+08:00",
                "EndTime": "2025-06-26T10:05:00+08:00"
            }
        ],
        "TotalCount": 1,
        "TaskInfo": {
            "Id": 10001,
            "TaskId": 10001,
            "FixStatus": 2,
            "AssetCount": 1,
            "SuccessCount": 1,
            "FailCount": 0,
            "FixingCount": 0,
            "QueueCount": 0,
            "Progress": 100,
            "SuccessVulCount": 1,
            "FailVulCount": 0,
            "VulNames": [
                "CVE-2024-12345"
            ],
            "VulFixStatusList": [
                {
                    "VulId": 20001,
                    "KBId": 0,
                    "VulName": "CVE-2024-12345",
                    "FixStatus": 1,
                    "HostCount": 1,
                    "SuccessHostCount": 1,
                    "FailHostCount": 0
                }
            ],
            "StartTime": "2025-06-26T10:00:00+08:00",
            "EndTime": "2025-06-26T10:05:00+08:00"
        },
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

