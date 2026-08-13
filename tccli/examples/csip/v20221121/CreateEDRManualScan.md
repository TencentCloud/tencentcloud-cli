**Example 1: tag模式创建任务**



Input: 

```
tccli csip CreateEDRManualScan --cli-unfold-argument  \
    --AssetSelectionType tag \
    --ScanType include \
    --MemberId mem-tencent-54213b157ddf7170 \
    --TagIds 139 \
    --CustomPaths /tmp \
    --Timeout 1800 \
    --EnableMemShellScan 0
```

Output: 
```
{
    "Response": {
        "Tasks": [
            {
                "AppId": 260199972,
                "TaskId": 304,
                "TaskType": "HOST"
            }
        ],
        "RequestId": "00dc20af-e070-4c80-b24c-becae48e73cb"
    }
}
```

