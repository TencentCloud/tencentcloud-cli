**Example 1: 查看镜像仓库定时扫描任务配置**



Input: 

```
tccli csip DescribeImageRegistryTimedScanTaskConfig --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "TaskInfo": [
            {
                "Enable": false,
                "Id": 3,
                "Name": "定时扫描任务_20260629114052_260083796",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "ScanType": [
                    "VIRUS"
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "335929c6-74db-4f87-8d19-8d5e27299dcf"
    }
}
```

