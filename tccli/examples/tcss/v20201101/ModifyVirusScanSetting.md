**Example 1: 运行时更新文件查杀设置**

运行时更新文件查杀设置

Input: 

```
tccli tcss ModifyVirusScanSetting --cli-unfold-argument  \
    --Timeout 5 \
    --BeginScanAt 10:59:00 \
    --Cycle 1 \
    --ScanPath /tmp \
    --ScanPathAll False \
    --ScanRangeAll False \
    --EnableScan True \
    --ScanIds ad297b24a4f818d9da49c9bec10d54c179b6751fc362802b077f710b3638e0f0 \
    --ScanPathType 0 \
    --ScanRangeType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b9cd345d-9d88-4e3b-86b6-e0e5c971731a"
    }
}
```

