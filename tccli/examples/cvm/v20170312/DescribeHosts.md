**Example 1: 查询CDH实例列表**

查询一个或多个CDH实例的详细信息

Input: 

```
tccli cvm DescribeHosts --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-6 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HostSet": [
            {
                "Placement": {
                    "Zone": "ap-guangzhou-6",
                    "ProjectId": 0
                },
                "HostId": "host-8th3ybbw",
                "HostType": "HM50",
                "HostName": "myHost",
                "CageId": "",
                "HostChargeType": "PREPAID",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "CreatedTime": "2024-09-30T03:17:49Z",
                "ExpiredTime": "2024-11-30T03:17:51Z",
                "InstanceIds": [
                    "ins-flx4u4ck",
                    "ins-p5s3wcq2"
                ],
                "HostState": "RUNNING",
                "Tags": [],
                "HostResource": {
                    "CpuTotal": 336,
                    "CpuAvailable": 18,
                    "MemTotal": 700,
                    "MemAvailable": 40,
                    "DiskTotal": 0,
                    "DiskAvailable": 0,
                    "DiskType": "",
                    "GpuTotal": 0,
                    "GpuAvailable": 0
                }
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

