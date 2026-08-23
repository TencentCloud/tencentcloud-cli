**Example 1: 查询镜像仓库镜像扫描任务列表**



Input: 

```
tccli csip DescribeImageRegistryScanTaskList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TaskList": [
            {
                "CancelReason": "手动取消",
                "FailureImageCount": 0,
                "Id": 2,
                "ImageIds": [
                    3
                ],
                "Name": "测试手动扫描任务",
                "OwnerAccountName": "700002365149",
                "OwnerAppId": 260083796,
                "OwnerUin": "700002365149",
                "ScanEndTime": "2026-06-29T22:50:51+08:00",
                "ScanImageCount": 0,
                "ScanStartTime": "2026-06-29T22:30:51+08:00",
                "ScanType": [
                    "MANUAL"
                ],
                "Status": 5,
                "SuccessImageCount": 0,
                "TimedScanConfigId": 0,
                "Timeout": 3600
            }
        ],
        "TotalCount": 1,
        "RequestId": "d6674432-32a8-414e-96fa-8cbb421447c6"
    }
}
```

