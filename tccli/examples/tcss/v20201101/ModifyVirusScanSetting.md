**Example 1: 运行时更新文件查杀设置**

运行时更新文件查杀设置

Input: 

```
tccli tcss ModifyVirusScanSetting --cli-unfold-argument  \
    --BeginScanAt xx \
    --EnableScan True \
    --ScanPathType 1 \
    --ScanRangeType 1 \
    --ScanPathAll True \
    --Timeout 1 \
    --ScanIds xx \
    --ScanPath xx \
    --ScanRangeAll True \
    --Cycle 1 \
    --ScanPathMode SCAN_PATH_ALL
```

Output: 
```
{
    "Response": {
        "RequestId": "b9cd345d-9d88-4e3b-86b6-e0e5c971731a"
    }
}
```

