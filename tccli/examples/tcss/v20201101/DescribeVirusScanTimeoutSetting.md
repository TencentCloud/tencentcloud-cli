**Example 1: 运行时文件扫描超时设置查询**



Input: 

```
tccli tcss DescribeVirusScanTimeoutSetting --cli-unfold-argument  \
    --ScanType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "33ec689a-e026-4700-8dc4-b559b97f0667",
        "Timeout": 5
    }
}
```

