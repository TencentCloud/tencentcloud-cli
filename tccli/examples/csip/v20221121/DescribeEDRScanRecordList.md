**Example 1: 查询MemberId数组对应账号创建的任务**



Input: 

```
tccli csip DescribeEDRScanRecordList --cli-unfold-argument  \
    --MemberId mem-tencent-54213b157ddf7170 \
    --Filter.Limit 10
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "AccountName": "",
                "AssetSelectionType": "all",
                "CloudType": 0,
                "CreateAppID": 260199972,
                "Creator": "700002653567",
                "CreatorCloudType": 0,
                "CreatorName": "管理_700002653567",
                "EndTime": "2026-08-11 18:23:59",
                "ScheduleDesc": "",
                "StartTime": "2026-08-11 17:28:24",
                "Status": "CANCELED",
                "TargetAppIDs": [
                    260199972
                ],
                "TaskId": 2324,
                "TaskName": "Malware_20260811172824_1",
                "TaskType": "HOST",
                "TotalAssetCount": 24,
                "TriggerType": "MANUAL"
            }
        ],
        "TotalCount": 857,
        "RequestId": "cde42a3c-bf57-4155-9ed1-3b6b23e3b361"
    }
}
```

