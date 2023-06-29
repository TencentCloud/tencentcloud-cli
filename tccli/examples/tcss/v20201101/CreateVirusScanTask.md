**Example 1: 运行时文件查杀一键扫描**

运行时文件查杀一键扫描

Input: 

```
tccli tcss CreateVirusScanTask --cli-unfold-argument  \
    --ScanRangeAll True \
    --ScanPathAll True \
    --ScanRangeType 1 \
    --ScanPathMode SCAN_PATH_DEFAULT \
    --Timeout 2
```

Output: 
```
{
    "Response": {
        "RequestId": "a6d8d540-940f-47d9-8d7f-daac832ba5b4",
        "TaskID": "6013a6c334b9a9000cf519be"
    }
}
```

