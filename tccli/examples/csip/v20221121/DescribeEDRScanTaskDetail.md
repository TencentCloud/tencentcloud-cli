**Example 1: 查询TaskId为4的扫描任务详情**



Input: 

```
tccli csip DescribeEDRScanTaskDetail --cli-unfold-argument  \
    --TaskId 4 \
    --MemberId mem-tencent-54213b157ddf7170 \
    --Filter.Limit 20 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "AccountName": "委派管理员1",
        "CloudType": 0,
        "ContainerList": null,
        "CreateAppID": 260199982,
        "CustomPaths": null,
        "EnableMemShellScan": 0,
        "EndTime": "",
        "FinishedAssetCount": 7,
        "HostList": [
            {
                "AccountName": "成员2",
                "AppId": 260082268,
                "CloudType": 0,
                "FailReason": "scan timeout",
                "FixSuggestion": "",
                "HostName": "1f665110",
                "InstanceId": "mix-qgbtrzf3",
                "OsType": "Ubuntu 24.04.4 LTS",
                "PrivateIp": "169.254.68.6",
                "PublicIp": "",
                "Quuid": "1f665110-706a-4f2c-bef7-9b0f15827419",
                "RiskCount": 0,
                "Status": "TIMEOUT"
            }
        ],
        "RiskAssetCount": 0,
        "ScanType": "full",
        "StartTime": "2026-07-07 15:16:17",
        "Status": "SCANNING",
        "TaskId": 4,
        "TaskName": "Malware_20260707_151616",
        "TaskType": "HOST",
        "Timeout": 3600,
        "TotalAssetCount": 7,
        "TotalCount": 7,
        "TriggerType": "MANUAL",
        "RequestId": "d2d353f4-6404-41bc-9c27-fbd351548f93"
    }
}
```

