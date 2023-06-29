**Example 1: 运行时更新文件查杀实时监控设置**

运行时更新文件查杀实时监控设置

Input: 

```
tccli tcss ModifyVirusMonitorSetting --cli-unfold-argument  \
    --EnableScan True \
    --ScanPathType 1 \
    --ScanPathAll True \
    --ScanPathMode SCAN_PATH_DEFAULT
```

Output: 
```
{
    "Response": {
        "RequestId": "b9cd345d-9d88-4e3b-86b6-e0e5c971731a"
    }
}
```

