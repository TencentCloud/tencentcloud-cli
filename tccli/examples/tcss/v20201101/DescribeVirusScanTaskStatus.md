**Example 1: 运行时查询文件查杀任务状态**

运行时查询文件查杀任务状态

Input: 

```
tccli tcss DescribeVirusScanTaskStatus --cli-unfold-argument  \
    --TaskID dskaldjskld
```

Output: 
```
{
    "Response": {
        "ContainerScanCnt": 0,
        "ContainerTotal": 339,
        "LeftSeconds": 4666,
        "RequestId": "b9e9e86e-5b7e-476c-9be1-a8c6399afef3",
        "RiskCnt": 0,
        "Schedule": 0,
        "Status": "SCANNING",
        "RiskContainerCnt": 0,
        "StartTime": "",
        "EndTime": "",
        "ScanType": 1
    }
}
```

